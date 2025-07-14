from typing import Optional
from fastapi import Depends, HTTPException
from src.services.starwars_service import get_character_with_most_films_service, get_planet_with_biggest_population_service, get_starwars_service, get_by_id_starwars_service
from src.models.starwars_interface import QueryParams

def get_starwars_controller(
    resource: str, 
    query_params: QueryParams = Depends(), 
    page: int = 1, 
):
    try: 
        data = get_starwars_service(resource, query_params, page)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
def get_by_id_starwars_controller(resource: str, id: int):
    try:
        data = get_by_id_starwars_service(resource, id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
