from config.path_config import *
from utils.common_function import read_yaml
from google.cloud import storage
from src.logger import get_log
from src.exceptions import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
logger = get_log(__name__)

class DataIngestion:
    def __init__(self):
        self.CONFIG_YAML = read_yaml(YAML_PATH)
        self.DATA_INGESTION_YAML = self.CONFIG_YAML["data-ingestion"]
        self.BUCKET_NAME = self.DATA_INGESTION_YAML["bucket-name"]
        self.BLOB_NAME = self.DATA_INGESTION_YAML["blob-name"]
        self.TRAIN_SIZE = self.DATA_INGESTION_YAML["train-size"]
        os.makedirs(RAW_PATH, exist_ok=True)
        
    def download_data(self):
        try:
            logger.info(f"Started to download data from GCP: {self.BUCKET_NAME}/{self.BLOB_NAME}")
            # Use service account key for authentication
            client = storage.Client.from_service_account_json("credentials.json")
            bucket = client.bucket(self.BUCKET_NAME)
            blob = bucket.blob(self.BLOB_NAME)
            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"Succesfully downloaded data from GCP: {self.BUCKET_NAME}/{self.BLOB_NAME}")
        except Exception as e:
            raise CustomException(f"Failed to downlaod data from GCP: {self.BUCKET_NAME}/{self.BLOB_NAME}",e)

    def ingestion_data(self):
        try:
            logger.info(f"Started read data from local: {RAW_FILE_PATH}")
            df = pd.read_csv(RAW_FILE_PATH)
            logger.info(f"Succesfully read data from local: {RAW_FILE_PATH}")
            train, test = train_test_split(df, train_size=self.TRAIN_SIZE, random_state=42)
            train.to_csv(RAW_TRAIN_PATH, index=False)
            logger.info(f"Ingested train data succesfully: {RAW_TRAIN_PATH}")
            test.to_csv(RAW_TEST_PATH,index=False)
            logger.info(f"Ingested test data succesfully: {RAW_TEST_PATH}")
        except Exception as e:
            raise CustomException(f"Faled to ingest data: {RAW_PATH}",e)
    def run(self):
        try:
            logger.info("Started data ingestion from GCP to Local Storage")
            self.download_data()
            self.ingestion_data()
            logger.info(f"Succesfully ingested data into: {RAW_PATH}")
        except CustomException as ce:
            logger.error(ce)

if __name__=="__main__":
    operation = DataIngestion()
    operation.run()