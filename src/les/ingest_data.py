import sys
from pathlib import Path
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from dataclasses import dataclass
from sklearn.preprocessing import train_test_split

@dataclass
class DataIngestionConfig:
    base_dir:str= Path(__file__).resolve().parent.parent.parent / 'artifacts'
    train_data_path: str = base_dir / 'train.csv'
    test_data_path: str = base_dir / 'test.csv'
    raw_data_path: str = base_dir / 'raw.csv'
    
    
class DataIngestion():
    def __init__(self):
        self.path=DataIngestionConfig()
        
    def read_csv(self):
        try:
            
            self.path.base_dir.mkdir(exists_ok=True)
            data=pd.read_csv('notebooks/stud.csv', index=False, header=True)
            logging.info("reading source data")
            data.to_csv(self.path.raw_data_path)
            logging.info("data stored in raw dires")
            train_set, test_set=train_test_split(data, test_size=.2, random_state=42)
            train_set.to_csv(self.path.train_data_path)
            test_set.to_csv(self.path.test_data_path)
            logging.info("data split it into test and train")
            return (
                self.path.train_data_path,
                self.path.test_data_path
                
            )
        except Exception as e:
            raise CustomException(e, sys)
        
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data, test_data=obj.read_csv()
    
    