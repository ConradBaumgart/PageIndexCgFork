import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from openai import AzureOpenAI, OpenAI
from pydantic import BaseModel

from app.logging_config import get_logger

logger = get_logger(__name__)

load_dotenv()
PROVIDER = os.getenv("LLM_PROVIDER")  # "mistral" or "azure"
TEMPERATURE = 0.0


@dataclass
class LLMResponse:
    content: str
    role: Optional[str]
    finish_reason: Optional[str]
    usage: Optional[Dict[str, int]]  # {'prompt_tokens':..., 'completion_tokens':..., 'total_tokens':...}
    model: Optional[str]
    created: Optional[int]
    raw_response: Any = None


class LLMClient:
    def __init__(self):
        self.provider = PROVIDER
        self.client, self.model = self._init_client()

    def _init_client(self):
        """
        Returns (client, model_name_or_deployment).
        All provider-specific details (endpoints, keys, model/deployment)
        are handled here so calls can be uniform later.
        """
        if self.provider == "mistral":
            client = OpenAI(
                api_key=os.getenv("MISTRAL_API_KEY"),
                base_url=os.getenv("MISTRAL_ENDPOINT"),
            )
            model = os.getenv("MISTRAL_MODEL")
            return client, model

        elif self.provider == "azure":
            client = AzureOpenAI(
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            )
            model = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
            return client, model

        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

    def generate(
        self,
        messages: List[Dict[str, str]],
        chat_history: List[Dict[str, str]] | None = None,
        json_response: Optional[bool] = False,
    ) -> LLMResponse:
        """
        messages: [{'role':'system'|'user'|'assistant', 'content': '...'}]
        Returns LLMResponse with provider-agnostic fields.
        """
        logger.info("LLM will be called with %s", str(messages)[:300])

        messages = (chat_history or []) + messages

        if json_response:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=TEMPERATURE,
                response_format={"type": "json_object"},
            )
        else:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=TEMPERATURE,
            )

        # Normalize usage as different models might return different usage metrics
        usage = None
        if getattr(resp, "usage", None):
            usage = {
                "prompt_tokens": getattr(resp.usage, "prompt_tokens", None),
                "completion_tokens": getattr(resp.usage, "completion_tokens", None),
                "total_tokens": getattr(resp.usage, "total_tokens", None),
            }

        primary = resp.choices[0]
        msg = getattr(primary, "message", None)

        logger.info("LLM returned %s", msg.content[:100])
        logger.debug("Full response of LLM is %r", resp)

        return LLMResponse(
            content=getattr(msg, "content", None),
            role=getattr(msg, "role", None),
            finish_reason=getattr(primary, "finish_reason", None),
            usage=usage,
            model=getattr(resp, "model", self.model),  # fall back to stored model/deployment
            created=getattr(resp, "created", None),
            raw_response=resp,
        )
