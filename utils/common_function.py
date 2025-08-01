import os
from yaml import safe_load
from src.logger import get_log
from src.exceptions import CustomException
logger = get_log(__name__)

def read_yaml(yaml_path):
    try:
        if not os.path.exists(yaml_path):
            raise FileNotFoundError(f"Not found the file:{yaml_path}")
        with open(yaml_path,"r") as file:
            yaml_content = safe_load(file)
            logger.info(f"Read yaml from {yaml_path} succesfully")
            return yaml_content
    except Exception as e:
        raise CustomException(f"Failed to load yaml: {read_yaml}",e)
    