# Aiza AI Assistant

Aiza is an AI assistant that integrates various APIs to provide functionalities such as weather updates, news, security insights, messaging, and more.

## Features

- **Weather API**: Get current weather information for any location.
- **News API**: Fetch the latest news based on your query.
- **Shodan API**: Search Shodan for security insights.
- **Twilio API**: Send messages using Twilio.
- **VirusTotal API**: Scan URLs for potential threats.
- **Google Custom Search API**: Perform custom searches on Google.
- **Captions.ai API**: Generate captions for images.

## Requirements

- Python 3.8+
- `requests` library
- `twilio` library
- `transformers` library
- `redis` library
- `speech_recognition` library
- `sentiment_analysis` library (or the correct one you are using)
- `pyyaml` library
- `tkinter` library
- An active internet connection

## Configuration

The application uses a `config.yaml` file to store API keys and other configuration details. Ensure you have all the necessary API keys.

### Sample `config.yaml`

```yaml
gemini_api: AIzaSyAlwkWeBUcBwot7nqMLZrliu3EccQCVanU
weather_api: 63f51f55360c424861b3440840e53456
weather_api_key: 5a7bf7247b39ecd69eeba132fbbb188e
news_api: b2fb4b06fed14eca9955a8923a251dc7
shodan_api: y3od0RTH5aVXMTzz1eiyqqpF4KB0fjUo
twilio_account_sid: MZTQ4SXQZ7576KDL5ELZLWKU
twilio_auth_token: your_twilio_auth_token
virustotal_api: c702523a174752a8ddc22fcebb677c47b0047e89d2f917d0bd73009e9c1f141b
google_custom_search_api: AIzaSyDooRaRAHIMwJDfa5rP63qgX3UZYG2yQuc
captions_ai: 400fb756-95fa-4822-8b67-b353a180fe98
```

## Setup

### Using `setup.sh`

You can use the provided `setup.sh` script to set up the project on a Linux system.

### Manual Setup

1. **Clone the Repository**:
   ```sh
   git clone git@github.com:yashraut369/Aiza.git
   cd Aiza
   ```

2. **Create and Activate Virtual Environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   pip install twilio transformers redis speech_recognition sentiment_analysis pyyaml requests tkinter
   ```

4. **Create `config.yaml`**:
   - Create a `config.yaml` file in the root directory of the project.
   - Copy the sample configuration provided above and replace the placeholder values with your actual API keys.

## Running the Application

You can run the Aiza AI assistant using the following command:

```sh
python main.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.