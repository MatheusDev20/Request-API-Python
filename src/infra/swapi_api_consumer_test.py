from .swapi_api_consumer import SwapiConsumer

def test_get_starships():
    """ Test get starships """
    swapi_consumer = SwapiConsumer()
    response = swapi_consumer.get_starships(page=1)

    print(response)
