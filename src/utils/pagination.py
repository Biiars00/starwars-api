from typing import Dict, Any, List
import math

def pagination(
    data: List[Dict[str, Any]], 
    page: int = 1
) -> Dict[str, Any]:
    page_size = 5

    total_items = len(data)
    total_pages = max(math.ceil(total_items / page_size), 1)

    if page < 1:
        page = 1
    page = min(page, total_pages)

    start = (page - 1) * page_size
    end = start + page_size

    items = data[start:end]

    return {
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
        "total_items": total_items,
        "items": items
    }
