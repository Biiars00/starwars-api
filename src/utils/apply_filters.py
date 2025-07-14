from typing import List, Dict, Any, Type
from pydantic import BaseModel

def apply_filters(
    data: List[Dict[str, Any]],
    filters: Dict[str, Any],
    model: Type[BaseModel],
) -> List[Dict[str, Any]]:
    filtered_data = data.copy()
    allowed_fields = model.model_fields.keys()

    for key, value in filters.items():
        if key in allowed_fields and value is not None:
            filtered_data = [
                item for item in filtered_data
                if str(item.get(key, "")).lower() == str(value).lower()
            ]
            
    return filtered_data
