import requests
import logging

class GeminiAPI:
    def __init__(self, config):
        self.api_key = config['gemini_api']

    def get_data(self, query):
        url = f"https://gemini.googleapis.com/v1/{query}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching data from Gemini API: {e}")
            return None