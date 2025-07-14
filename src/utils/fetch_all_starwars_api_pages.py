from typing import List, Dict, Any, Optional
from src.gateways.api_gateway import fetch_starwars_api

def fetch_all_starwars_api_pages(endpoint: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    all_results = []
    page = 1

    while True:
        current_params = params.copy() if params else {}
        current_params["page"] = page

        data = fetch_starwars_api(endpoint, params=current_params)

        if "error" in data:
            raise ValueError(f"Erro ao buscar página {page} de {endpoint}: {data['error']}")

        if "results" in data:
            all_results.extend(data["results"])

            if not data.get("next"):
                break
            page += 1
        else:
            if isinstance(data, list):
                all_results.extend(data)
            else:
                raise ValueError(f"Unexpected format returned from {endpoint}: {data}")
            break

    return all_results
