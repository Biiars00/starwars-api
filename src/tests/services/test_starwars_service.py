from unittest.mock import patch
from src.models.starwars_interface import QueryParams
from src.services import starwars_service

@patch("src.services.starwars_service.fetch_all_starwars_api_pages")
def test_get_starwars_service(mock_fetch):
    mock_data = [
        {
            'title': 'The Phantom Menace',
            'episode_id': 1,
            'opening_crawl': 'Turmoil has engulfed the Galactic Republic...',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19',
            'characters': ['https://swapi.dev/api/people/2/'],
            'planets': ['https://swapi.dev/api/planets/1/'],
            'starships': ['https://swapi.dev/api/starships/31/'],
            'vehicles': ['https://swapi.dev/api/vehicles/33/'],
            'species': ['https://swapi.dev/api/species/1/']
        }
    ]
    
    mock_fetch.return_value = mock_data
    
    resource = "films"
    query_params = QueryParams(name=None, order_by="title", order="asc")
    page = 1

    result = starwars_service.get_starwars_service(resource, query_params, page)
    
    assert result["page"] == 1
    assert result["page_size"] == 5
    assert result["total_pages"] == 1
    assert result["total_items"] == 1 
    assert result["items"] == mock_data
    
@patch("src.services.starwars_service.fetch_starwars_api")
def test_get_by_id_starwars_service(mock_fetch):
    mock_fetch.return_value = {
        'title': 'The Phantom Menace',
        'episode_id': 1,
        'opening_crawl': 'Turmoil has engulfed the\r\nGalactic Republic...',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '1999-05-19',
        'characters': ['https://swapi.dev/api/people/2/'],
        'planets': ['https://swapi.dev/api/planets/1/'],
        'starships': ['https://swapi.dev/api/starships/31/'],
        'vehicles': ['https://swapi.dev/api/vehicles/33/'],
        'species': ['https://swapi.dev/api/species/1/']
    }
    
    resource = 'films'
    id = 4

    result = starwars_service.get_by_id_starwars_service(resource, id)

    assert result == mock_fetch.return_value
    mock_fetch.assert_called_once_with(f"{resource}/{id}")