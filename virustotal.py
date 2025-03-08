import requests
import logging

class VirusTotalAPI:
    def __init__(self, config):
        self.api_key = config['virustotal_api']

    def scan_url(self, url_to_scan):
        url = "https://www.virustotal.com/vtapi/v2/url/scan"
        params = {'apikey': self.api_key, 'url': url_to_scan}
        try:
            response = requests.post(url, data=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error scanning URL with VirusTotal: {e}")
            return None