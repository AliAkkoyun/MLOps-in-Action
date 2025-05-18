import os
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.custom_exception import CustomException
from src.logger import get_logger
from config.paths_config import *
from config.paths_config import *
from utils.common_functions import read_yaml_file
import sys

logger = get_logger(__name__)   

def divide_two_numbers(a, b):
    try:
        result = a / b
        logger.info(f"Division successful: {result}")
        return result
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise CustomException("Custom error occured", sys)
    
if __name__ == "__main__":
    try:
        divide_two_numbers(10, 1)
    except CustomException as ce:
        logger.error(str(ce))
