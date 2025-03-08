import requests
import logging

class CaptionsAI:
    def __init__(self, config):
        self.api_key = config['captions_ai']

    def generate_caption(self, image_path):
        url = "https://api.captions.ai/v1/caption"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        files = {'file': open(image_path, 'rb')}
        try:
            response = requests.post(url, headers=headers, files=files)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error generating caption with Captions.ai: {e}")
            return None