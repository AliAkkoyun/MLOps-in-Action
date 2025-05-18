import os


############################# DATA INGESTION #############################

RAW_DIR = os.path.join("artifacts", "raw")
RAW_FILE_PATH = os.path.join(RAW_DIR, "data.csv")
TRAIN_FILE_PATH = os.path.join(RAW_DIR, "train.csv")    
TEST_FILE_PATH = os.path.join(RAW_DIR, "test.csv")

CONFIG_PATH = "config/config.yaml"