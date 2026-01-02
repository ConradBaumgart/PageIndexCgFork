"""
Uses the OpenAPI documentation in openapi.json to create a Markdown version and adds it to README.md file.
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

MD_TITLE = "## API Reference"
README_START = "<!-- AUTO-GENERATED-OPENAPI:START -->"
README_END = "<!-- AUTO-GENERATED-OPENAPI:END -->"


def _md_escape(text: str) -> str:
    return text.replace("|", r"\|").replace("<", "&lt;").replace(">", "&gt;")


def _schema_name(ref: str) -> str:
    # e.g., "#/components/schemas/Order" -> "Order"
    return ref.split("/")[-1]


def _render_schema(schema: Dict[str, Any], components: Dict[str, Any], depth: int = 0) -> str:
    """Render a JSON schema into a compact Markdown table."""
    if not schema:
        return ""
    lines: List[str] = []
    indent = ""  # keep flat for Markdown

    if "$ref" in schema:
        name = _schema_name(schema["$ref"])
        lines.append(f"**Schema**: `{name}`")
        resolved = components.get("schemas", {}).get(name, {})
        if resolved:
            lines.append(_render_schema(resolved, components, depth + 1))
        return "\n".join(lines)

    typ = schema.get("type")
    fmt = schema.get("format")
    desc = schema.get("description")
    if typ:
        lines.append(f"- **type**: `{typ}`" + (f" (`{fmt}`)" if fmt else ""))
    if desc:
        lines.append(f"- **description**: {_md_escape(desc)}")

    if typ == "array":
        items = schema.get("items", {})
        lines.append("- **items**:")
        lines.append(_render_schema(items, components, depth + 1))

    props = schema.get("properties") or {}
    required = set(schema.get("required") or [])
    if props:
        lines.append("\n**Properties**")
        lines.append("| Name | Type | Required | Description |")
        lines.append("|------|------|----------|-------------|")
        for name, prop in props.items():
            # resolve $ref
            if "$ref" in prop:
                ref_name = _schema_name(prop["$ref"])
                typ_str = f"{ref_name})"
                # Inline minimal info
                desc = prop.get("description", "")
            else:
                ptype = prop.get("type", "object")
                fmt = prop.get("format")
                typ_str = f"`{ptype}`" + (f" (`{fmt}`)" if fmt else "")
                desc = prop.get("description", "")
            lines.append(f"| `{name}` | {typ_str} | {'yes' if name in required else 'no'} | {_md_escape(desc or '')} |")

    # examples
    example = schema.get("example")
    if example is None and "examples" in schema and isinstance(schema["examples"], list) and schema["examples"]:
        example = schema["examples"][0]
    if example is not None:
        import json as _json

        lines.append("\n**Example**")
        lines.append("```json")
        lines.append(_json.dumps(example, ensure_ascii=False, indent=2))
        lines.append("```")

    return "\n".join(lines)


def _render_parameters(params: List[Dict[str, Any]], components: Dict[str, Any]) -> str:
    if not params:
        return ""
    lines = [
        "**Parameters**",
        "",
        "| Name | In | Required | Type | Description |",
        "|------|----|----------|------|-------------|",
    ]
    for p in params:
        name = p.get("name", "")
        _in = p.get("in", "")
        req = "yes" if p.get("required") else "no"
        schema = p.get("schema", {})
        typ = schema.get("type", "") or (f"[{_schema_name(schema['$ref'])}]" if "$ref" in schema else "")
        desc = p.get("description", "") or ""
        lines.append(f"| `{name}` | `{_in}` | {req} | `{typ}` | {_md_escape(desc)} |")
    return "\n".join(lines)


def _render_request_body(rb: Dict[str, Any], components: Dict[str, Any]) -> str:
    if not rb:
        return ""
    lines = ["**Request Body**"]
    desc = rb.get("description")
    if desc:
        lines.append(_md_escape(desc))
    content = rb.get("content", {})
    for ctype, spec in content.items():
        lines.append(f"\n_Content-Type_: `{ctype}`\n")
        schema = spec.get("schema", {})
        lines.append(_render_schema(schema, components))
    return "\n".join(lines)


def _render_responses(responses: Dict[str, Any], components: Dict[str, Any]) -> str:
    if not responses:
        return ""
    lines = ["**Responses**"]
    for status, resp in responses.items():
        lines.append(f"\n- **{status}**: {_md_escape(resp.get('description', ''))}")
        content = resp.get("content", {})
        for ctype, spec in content.items():
            lines.append(f"  - _Content-Type_: `{ctype}`")
            schema = spec.get("schema", {})
            rendered = _render_schema(schema, components)
            if rendered.strip():
                lines.append(rendered)
    return "\n".join(lines)


def openapi_to_markdown(schema: Dict[str, Any]) -> str:
    info = schema.get("info", {})
    title = info.get("title", "API")
    version = info.get("version", "")
    desc = info.get("description", "")

    md: List[str] = []
    md.append(MD_TITLE)
    md.append("")
    md.append(f"**{_md_escape(title)}** (v{_md_escape(version)})")
    if desc:
        md.append("")
        md.append(_md_escape(desc))

    tags = {t["name"]: t.get("description", "") for t in schema.get("tags", []) if "name" in t}

    paths = schema.get("paths", {})
    components = schema.get("components", {})

    # Sort paths + methods for stable output
    for path in sorted(paths.keys()):
        md.append(f"\n### `{path}`")
        methods = paths[path]
        for method in sorted(methods.keys()):
            op = methods[method]
            op_id = op.get("operationId", f"{method}_{path}")
            summary = op.get("summary", "")
            description = op.get("description", "")
            op_tags = op.get("tags", [])
            md.append(f"\n#### {method.upper()}")
            if summary:
                md.append(f"**Summary**: {_md_escape(summary)}")
            if op_tags:
                md.append(f"**Tags**: {', '.join(f'`{t}`' for t in op_tags)}")
                # Include tag descriptions inline (nice in README)
                for t in op_tags:
                    if tags.get(t):
                        md.append(f"> {_md_escape(tags[t])}")
            if description:
                md.append(f"\n{_md_escape(description)}")

            # parameters
            params = op.get("parameters", [])
            p_block = _render_parameters(params, components)
            if p_block:
                md.append("\n" + p_block)

            # request body
            rb = op.get("requestBody", {})
            rb_block = _render_request_body(rb, components)
            if rb_block:
                md.append("\n" + rb_block)

            # responses
            resp_block = _render_responses(op.get("responses", {}), components)
            if resp_block:
                md.append("\n" + resp_block)

    return "\n".join(md).strip() + "\n"


def update_readme_section(readme_path: Path, content: str) -> None:
    original = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
    block = f"{README_START}\n\n{content}\n{README_END}"

    if README_START in original and README_END in original:
        new = re.sub(
            rf"{re.escape(README_START)}.*?{re.escape(README_END)}",
            block,
            original,
            flags=re.DOTALL,
        )
    else:
        # Append with a small heading if markers missing
        if original and not original.endswith("\n"):
            original += "\n"
        new = original + "\n" + block + "\n"

    readme_path.write_text(new, encoding="utf-8")
    print(f"✅ Updated {readme_path.resolve()}")


def main():
    schema = json.loads(Path("openapi.json").read_text(encoding="utf-8"))
    md = openapi_to_markdown(schema)
    update_readme_section(Path("README.md"), md)


if __name__ == "__main__":
    main()
