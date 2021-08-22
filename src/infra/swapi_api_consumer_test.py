from .swapi_api_consumer import SwapiConsumer

def test_get_starships(requests_mock):
    """ Test get starships """
    requests_mock.get('https://swapi.dev/api/starships', status_code=200, json={"some": "thing"})
    swapi_consumer = SwapiConsumer()
    response = swapi_consumer.get_starships(page=1)

    print(response)
