"""
Generates an OpenAPI documentation under openapi.json
"""

import json
import os
from pathlib import Path

from fastapi.openapi.utils import get_openapi

print("Current working directory:", os.getcwd())
# Import your app object
# Adjust the import path to your project, e.g., from app.main import app
from app.main import app  # <-- change if your app module differs


def build_openapi_schema():
    # Allow your app to skip side-effects during import if you use such a guard
    os.environ.setdefault("GENERATING_OPENAPI", "1")
    schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    return schema


def main():
    out = Path("openapi.json")
    schema = build_openapi_schema()
    out.write_text(json.dumps(schema, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Wrote {out.resolve()}")


if __name__ == "__main__":
    main()
