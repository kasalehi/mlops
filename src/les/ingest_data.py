import sys
from pathlib import Path
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str= 