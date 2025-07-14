import requests
from typing import Any, Dict, Optional
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_starwars_api(endpoint: str = "", params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    base_url = 'https://swapi.dev/api'
    url = f'{base_url}/{endpoint}'

    try:
        response = requests.get(url, params=params, verify=False, timeout=10)
        response.raise_for_status()
        
        if 'application/json' in response.headers.get('Content-Type', ''):
            return response.json()
        else:
            return {"error": "Response is not JSON", "content": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}