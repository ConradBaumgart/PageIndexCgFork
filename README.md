# 🌲 PageIndex Fork for RhAI
PageIndex can transform lengthy PDF documents into a semantic tree structure. This repository is a fork of [VectifyAI-PageIndex](https://github.com/VectifyAI/PageIndex).

<details>
<summary><strong>Here is an example output.</strong></summary>

```jsonc
...
{
  "doc_name": "MIL-STD-1316F.pdf",
  "doc_description": "This document is a comprehensive design criteria standard for fuze safety and arming systems in military munitions, detailing requirements for explosive materials, safety features, environmental resilience, and compliance with international agreements.",
  "structure": [
    {
      "title": "Preface",
      "start_index": 1,
      "end_index": 8,
      "node_id": "0000",
      "text": "MIL -STD -1316F  \n18 August 2017  \n \nSUPERSEDING  \nMIL -STD -1316E  \n10 JULY  1998  \n \n \nDEPARTMENT OF DEFENSE  \nDESIGN CRITERIA STANDARD ...",
      "summary": "The partial document is a section of MIL-STD-1316F, a design criteria standard for fuze design and safety criteria issued by ..."
    },
    {
      "title": "SCOPE",
      "start_index": 8,
      "end_index": 8,
      "nodes": [
        {
          "title": "Scope",
          "start_index": 8,
          "end_index": 8,
          "node_id": "0002",
          "text": "MIL-STD -1316F  \n1 \n 1. SCOPE  \n1.1 Scope .  This standard establishes ...",
          "summary": "The partial document outlines the scope and applicability of the MIL-STD-1316F standard, which establishes design safety criteria for fuzes and ..."
        },
        {
          "title": "Applicability",
          "start_index": 8,
          "end_index": 8,
          "node_id": "0003",
          "text": "... 1.2 Applicability .  This standard applies to the design of fuzes and S&A devices ...",
          "summary": "The partial document outlines the scope and applicability of the MIL-STD-1316F standard, which establishes design safety criteria for fuzes and ..."
        }
      ]
    }
}
...
```
</details>

## Configs

| File                             | Settings 
| -------------------------------- | ---
| .env file                        | which model and access credentials
| app/models/page_index_options.py | detailed settings for PageIndex e.g. how many pages to scan for a table of content


## DevOps

For Development:
- Create an .env file according to the env-example file
- Run as FastAPI app e.g. with `uv run uvicorn app.main:app --host 0.0.0.0 --port 8000`
- Run ruff checks with `uv run ruff format .` and `uv run ruff check . --fix`

For Deployment:
- Use the dockerfile to build the image
- Start an container e.g. with `podman run -d -p 8001:8001 --name my-container my-image:latest`
- Call endpoints e.g. with `curl -H "Accept: application/json" http://localhost:8001/list_available_documents`


<!-- AUTO-GENERATED-OPENAPI:START -->

## API Reference

**Information Retrieval Service** (v0.1.0)

### `/health_check`

#### GET
**Summary**: Health Check

**Responses**

- **200**: Successful Response
  - _Content-Type_: `application/json`
- **type**: `object`

### `/list_available_documents`

#### GET
**Summary**: List Available Documents

List all documents which are available for information retrieval.

**Responses**

- **200**: Successful Response
  - _Content-Type_: `application/json`
- **type**: `array`
- **items**:
- **type**: `object`

### `/query_documents`

#### GET
**Summary**: Query Documents

Return content from documents relevant to the query.
Currently, information will be retrieved from 1 document. The document with the most relevance for the query will be used.

**Parameters**

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `query` | `query` | yes | `string` | The question or search query |
| `documents` | `query` | yes | `array` | List of document names (repeat this query param) |

**Responses**

- **200**: Successful Response
  - _Content-Type_: `application/json`
- **type**: `array`
- **items**:
- **type**: `object`

- **422**: Validation Error
  - _Content-Type_: `application/json`
**Schema**: `HTTPValidationError`
- **type**: `object`

**Properties**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `detail` | `array` | no |  |

### `/upload_document`

#### POST
**Summary**: Upload Document

Upload a single PDF document to process it and make it available for information retrieval.

**Request Body**

_Content-Type_: `multipart/form-data`

**Schema**: `Body_upload_document_upload_document_post`
- **type**: `object`

**Properties**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file` | `string` (`binary`) | yes |  |

**Responses**

- **200**: Successful Response
  - _Content-Type_: `application/json`
- **type**: `object`

- **422**: Validation Error
  - _Content-Type_: `application/json`
**Schema**: `HTTPValidationError`
- **type**: `object`

**Properties**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `detail` | `array` | no |  |

<!-- AUTO-GENERATED-OPENAPI:END -->
