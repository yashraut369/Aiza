import requests
import logging

class NewsAPI:
    def __init__(self, config):
        self.api_key = config['news_api']

    def get_news(self, query):
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching news data: {e}")
            return None