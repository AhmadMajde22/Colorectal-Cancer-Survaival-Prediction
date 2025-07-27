from src.data_ingestion import DataIngestion
from src.data_processing import DataProcessing
from src.model_training import ModelTraining


from utils.common_functions import read_yaml, read_json_credentials
from src.logger import get_logger
from config.path_config import CONFIG_PATH, CREDENTIALS_PATH
import mlflow

logger = get_logger(__name__)

if __name__ == "__main__":
    
    config = read_yaml(CONFIG_PATH)
    credentials = read_json_credentials(CREDENTIALS_PATH)
    data_ingestion = DataIngestion(config=config, credentials=credentials)
    data_ingestion.run()

    input_path = r"artifacts/raw/data.csv"
    output_path = r"artifacts/processed"

    processer = DataProcessing(input_path,output_path)

    processer.run()

    with mlflow.start_run():
        trainier = ModelTraining()
        trainier.run()
        logger.info("Training Pipeline completed successfully.")
        
