import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv

load_dotenv()
PROVIDER = os.getenv("LLM_PROVIDER")  # "mistral" or "azure"


@dataclass
class UnifiedChatChoice:
    index: int
    content: str
    role: Optional[str] = None
    finish_reason: Optional[str] = None
    tool_calls: Optional[List[Dict[str, Any]]] = None


@dataclass
class UnifiedChatResponse:
    content: str
    role: Optional[str]
    finish_reason: Optional[str]
    usage: Optional[Dict[str, int]]  # {'prompt_tokens':..., 'completion_tokens':..., 'total_tokens':...}
    model: Optional[str]
    created: Optional[int]
    choices: Optional[List[UnifiedChatChoice]] = None
    stop_reason: Optional[str] = None
    raw_response: Any = None


class LLMClient:
    def __init__(self):
        self.provider = PROVIDER
        self.client = self._init_client()

    def _init_client(self):
        if self.provider == "mistral":
            from openai import OpenAI

            return OpenAI(
                api_key=os.getenv("MISTRAL_API_KEY"),
                base_url=os.getenv("MISTRAL_ENDPOINT"),
            )
        elif self.provider == "azure":
            from langchain_openai import AzureChatOpenAI

            return AzureChatOpenAI(
                openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
                azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
                temperature=0,
            )
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

    def generate(self, messages: List[Dict[str, str]]) -> UnifiedChatResponse: # Change to use string for messages as it is simplier to call
        """
        messages: List[{'role': 'system'|'user'|'assistant', 'content': '...'}]
        Returns UnifiedChatResponse with provider-agnostic fields.
        """
        if self.provider == "mistral":
            model = os.getenv("MISTRAL_MODEL")
            resp = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0,
            )
            choice = resp.choices[0]
            finish_reason = getattr(choice, "finish_reason", None)
            usage = None
            if getattr(resp, "usage", None):
                usage = {
                    "prompt_tokens": resp.usage.prompt_tokens,
                    "completion_tokens": resp.usage.completion_tokens,
                    "total_tokens": resp.usage.total_tokens,
                }

            choices = []
            for idx, ch in enumerate(resp.choices):
                choices.append(
                    UnifiedChatChoice(
                        index=idx,
                        content=ch.message.content,
                        role=getattr(ch.message, "role", None),
                        finish_reason=getattr(ch, "finish_reason", None),
                        tool_calls=getattr(ch.message, "tool_calls", None),
                    )
                )

            return UnifiedChatResponse(
                content=choice.message.content,
                role=getattr(choice.message, "role", None),
                finish_reason=finish_reason,
                usage=usage,
                model=getattr(resp, "model", None),
                created=getattr(resp, "created", None),
                choices=choices,
                stop_reason=finish_reason,
                raw_response=resp,
            )

        elif self.provider == "azure":
            # Convert OpenAI-style messages to a prompt or LangChain messages.
            # Simple approach: join into a single string prompt.
            prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
            ai_msg = self.client.invoke(prompt)

            # Extract content, usage, and finish_reason from AIMessage
            content = getattr(ai_msg, "content", "")
            usage_meta = getattr(ai_msg, "usage_metadata", None)
            resp_meta = getattr(ai_msg, "response_metadata", {}) or {}

            # finish_reason sits in response_metadata
            finish_reason = resp_meta.get("finish_reason")
            # usage: prefer usage_metadata, else token_usage under response_metadata
            usage = None
            if isinstance(usage_meta, dict):
                # usage_metadata: {'input_tokens':..., 'output_tokens':..., 'total_tokens':...}
                # normalize to OpenAI-like keys
                usage = {
                    "prompt_tokens": usage_meta.get("input_tokens"),
                    "completion_tokens": usage_meta.get("output_tokens"),
                    "total_tokens": usage_meta.get("total_tokens"),
                }
            else:
                token_usage = resp_meta.get("token_usage")
                if isinstance(token_usage, dict):
                    usage = {
                        "prompt_tokens": token_usage.get("prompt_tokens"),
                        "completion_tokens": token_usage.get("completion_tokens"),
                        "total_tokens": token_usage.get("total_tokens"),
                    }

            model_name = resp_meta.get("model_name") or os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

            return UnifiedChatResponse(
                content=content,
                role="assistant",  # LangChain AIMessage is an assistant message
                finish_reason=finish_reason,
                usage=usage,
                model=model_name,
                created=None,
                choices=[UnifiedChatChoice(index=0, content=content, role="assistant", finish_reason=finish_reason)],
                stop_reason=finish_reason,
                raw_response=ai_msg,
            )
