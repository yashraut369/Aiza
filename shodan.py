import requests
import logging

class ShodanAPI:
    def __init__(self, config):
        self.api_key = config['shodan_api']

    def search(self, query):
        url = f"https://api.shodan.io/shodan/host/search?key={self.api_key}&query={query}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error searching Shodan: {e}")
            return None