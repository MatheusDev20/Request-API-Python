import requests

class SwapiConsumer:
    """ Class to make external Requests to Swapi API"""
    @classmethod
    def get_starships(self, page: int) -> any:
        """ Get Starships """
        params = {'page': page}
        response = requests.get('https://swapi.dev/api/starships', params=params)

        return response.json()