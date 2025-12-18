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

env: which model and access credentials


<details>
<summary><strong>Optional parameters</strong></summary>
<br>
You can customize the processing with additional optional arguments:

```
--model                 OpenAI model to use (default: gpt-4o-2024-11-20)
--toc-check-pages       Pages to check for table of contents (default: 20)
--max-pages-per-node    Max pages per node (default: 10)
--max-tokens-per-node   Max tokens per node (default: 20000)
--if-add-node-id        Add node ID (yes/no, default: yes)
--if-add-node-summary   Add node summary (yes/no, default: yes)
--if-add-doc-description Add doc description (yes/no, default: yes)
```
</details>


## Operations
run as fast api backend
provide .env file
use dockerfile for 
ask Alpcan for Feedback

## API

