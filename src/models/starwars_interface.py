from pydantic import BaseModel
from typing import List, Optional

class StarWarsPeople(BaseModel):
    name: str
    height: Optional[str]
    mass: Optional[str]
    hair_color: Optional[str]
    skin_color: Optional[str]
    eye_color: Optional[str]
    birth_year: Optional[str]
    gender: Optional[str]
    homeworld: Optional[str]
    films: List[str]
    species: List[str]
    vehicles: List[str]
    starships: List[str]
    
class StarWarsFilms(BaseModel):
    title: str
    episode_id: Optional[int]
    opening_crawl: Optional[str]
    director: Optional[str]
    producer: Optional[str]
    release_date: Optional[str]
    characters: List[str]
    planets: List[str]
    starships: List[str]
    vehicles: List[str]
    species: List[str]
    
class StarWarsPlanets(BaseModel):
    name: str
    rotation_period: Optional[str]
    orbital_period: Optional[str]
    diameter: Optional[str]
    climate: Optional[str]
    gravity: Optional[str]
    terrain: Optional[str]
    surface_water: Optional[str]
    population: Optional[str]
    residents: List[str]
    films: List[str]
    
class StarWarsSpecies(BaseModel):
    name: str
    classification: Optional[str]
    designation: Optional[str]
    average_height: Optional[str]
    skin_colors: Optional[str]
    hair_colors: Optional[str]
    eye_colors: Optional[str]
    average_lifespan: Optional[str]
    homeworld: Optional[str]
    language: Optional[str]
    people: List[str]
    films: List[str]
    
class StarWarsVehicles(BaseModel):
    name: str
    model: Optional[str]
    manufacturer: Optional[str]
    cost_in_credits: Optional[str]
    length: Optional[str]
    max_atmosphering_speed: Optional[str]
    crew: Optional[str]
    passengers: Optional[str]
    cargo_capacity: Optional[str]
    consumables: Optional[str]
    vehicle_class: Optional[str]
    pilots: List[str]
    films: List[str]
    
class StarWarsStarships(BaseModel):
    name: str
    model: Optional[str]
    manufacturer: Optional[str]
    cost_in_credits: Optional[str]
    length: Optional[str]
    max_atmosphering_speed: Optional[str]
    crew: Optional[str]
    passengers: Optional[str]
    cargo_capacity: Optional[str]
    consumables: Optional[str]
    hyperdrive_rating: Optional[str]
    MGLT: Optional[str]
    starship_class: Optional[str]
    pilots: List[str]
    films: List[str]
    
RESOURCE_MODEL_MAP = {
    "characters": StarWarsPeople,
    "films": StarWarsFilms,
    "planets": StarWarsPlanets,
    "species": StarWarsSpecies,
    "vehicles": StarWarsVehicles,
    "starships": StarWarsStarships,
}

class QueryParams(BaseModel):
    name: Optional[str] = None
    order_by: Optional[str] = None
    order: Optional[str] = "asc"