from src.gateways.api_gateway import fetch_starwars_api
from src.models.starwars_interface import RESOURCE_MODEL_MAP, QueryParams
from src.utils.pagination import pagination
from src.utils.fetch_all_starwars_api_pages import fetch_all_starwars_api_pages
from src.utils.apply_filters import apply_filters

def get_starwars_service(
    resource: str, 
    query_params: QueryParams, 
    page: int = 1
):
    params = {}

    if query_params.name:
        params['search'] = query_params.name
        
    data = fetch_all_starwars_api_pages(resource, params=params)
    
    model = RESOURCE_MODEL_MAP.get(resource)
    
    if resource == 'films':
        if query_params.order_by == 'title':
            reverse = query_params.order == 'desc'
            data = sorted(data, key=lambda x: x.get('title', ''), reverse=reverse)
    else:
        if query_params.order_by == 'name':
            reverse = query_params.order == 'desc'
            data = sorted(data, key=lambda x: x.get('name', ''), reverse=reverse)
            
    if model:
        filters = query_params.model_dump(exclude_none=True)
        filters.pop("order_by", None)
        filters.pop("order", None)
        
        data = apply_filters(data, filters, model)
    
    result = pagination(data, page=page)
    
    return result

def get_by_id_starwars_service(resource: str, id: int):
    endpoint = f'{resource}/{id}'
    data = fetch_starwars_api(endpoint)
    return data