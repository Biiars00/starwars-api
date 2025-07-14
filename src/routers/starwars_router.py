from fastapi import APIRouter, Depends, Query
from src.models.starwars_interface import QueryParams
from src.config.auth.firebase_auth import verify_token
from src.controllers.starwars_controller import (
    get_character_with_most_films_controller,
    get_planet_with_biggest_population_controller,
    get_starwars_controller, 
    get_by_id_starwars_controller
)

starwars_router = APIRouter()

@starwars_router.get('/starwars/{resource}', tags=["Star Wars"])
async def fetch_starwars(
    resource: str,
    name: str = Query(None),
    order_by: str = Query(None),
    order: str = Query("asc"),
    page: int = Query(1),
    uid: str = Depends(verify_token)
):
    query_params = QueryParams(
        name=name,
        order_by=order_by,
        order=order
    )
    
    data = get_starwars_controller(resource, query_params, page)
    return data

@starwars_router.get('/starwars/{resource}/{id}', tags=["Star Wars"])
async def fetch_starwars_by_id(
    resource: str,
    id: int,
    uid: str = Depends(verify_token)
):
    return get_by_id_starwars_controller(resource, id)

