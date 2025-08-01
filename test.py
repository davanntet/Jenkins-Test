from src.logger import get_log
from src.exceptions import CustomException
import sys
logger = get_log(__name__)

def divice(a,b):
    try:
        logger.info("Calculating on divide")
        result = a/b
        print(result)
    except Exception as e:
        logger.error("Error on divide: can't divice by 0")
        raise CustomException("Can not deivce by 0", sys)
    
if __name__=="__main__":
    try:
        logger.info("Start calculating")
        divice(2,0)
        logger.info("Calculating is successfully")
    except CustomException as ce:
        logger.error(ce)