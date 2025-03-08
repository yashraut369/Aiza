import requests
import logging

class GoogleSearchAPI:
    def __init__(self, config):
        self.api_key = config['google_custom_search_api']

    def search(self, query, cx):
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={self.api_key}&cx={cx}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error performing Google Custom Search: {e}")
            return None