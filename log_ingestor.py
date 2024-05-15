import requests
import logging
import yaml
import time
from datetime import datetime

# Load configuration
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Configure logging
def configure_logging():
    for api_config in config['apis']:
        log_file = api_config['log_file']
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(message)s')

# Fetch logs from APIs
def fetch_logs():
    for api_config in config['apis']:
        url = api_config['url']
        log_file = api_config['log_file']
        try:
            response = requests.get(url)
            response.raise_for_status()
            logs = response.json()
            for log in logs:
                log_entry = {
                    "level": log.get("level", "info"),
                    "log_string": log.get("log_string", ""),
                    "timestamp": log.get("timestamp", datetime.utcnow().isoformat() + "Z"),
                    "metadata": {
                        "source": log_file
                    }
                }
                with open(log_file, 'a') as f:
                    f.write(f"{log_entry}\n")
        except requests.RequestException as e:
            logging.error(f"Error fetching logs from {url}: {e}")

if __name__ == "__main__":
    configure_logging()
    while True:
        fetch_logs()
        time.sleep(config['fetch_interval'])
