import os

# Path for Data INGESTION
RAW_DIR = "artifacts/raw"
RAW_FILE_PATH = os.path.join(RAW_DIR, 'raw.csv')

os.makedirs(RAW_DIR, exist_ok=True)


CONFIG_PATH = "config/config.yaml"
CREDENTIALS_PATH = "config/credentials.json"
