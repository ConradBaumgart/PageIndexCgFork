
from dataclasses import dataclass

@dataclass
class PageIndexOptions:
    model: str = "mistral-large-2411"
    toc_check_page_num: int = 20
    max_page_num_each_node: int = 10
    max_token_num_each_node: int = 20000
    if_add_node_id: str = "yes"
    if_add_node_summary: str = "yes"
    if_add_doc_description: str = "yes"
    if_add_node_text: str = "yes"
