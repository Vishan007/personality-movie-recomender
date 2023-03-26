import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

"""
These data classes hold certain properties and 
functions to deal specifically with the data and its representation.
""" 
logging.info('All the modules are imported')

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"raw.csv")

logging.info('data class is created')
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()   ##the above three paths will be saved in this variable
        logging.info('init function is called')

    def initiate_data_ingestion(self):   ##this function is used to read the dataset from the database
        logging.info("Entered in the dataingestion process.")
        try:  ##we can use any database to read the data from this function sql or mongodb
            df = pd.read_csv(r'C:\Users\HP\Desktop\Projects\end to end 1\data\16P.csv' , encoding='latin-1' , index_col='Response Id')    ##reading the data frame

            logging.info('Reading the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)  #making the directory for train data

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)  ##saving the data in csv format

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=3)  ##spliting the dataset in train and test data

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)  ##saving the train data to csv

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)  ##saving the test data to csv

            logging.info('Dataingestion is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e , sys)
        
if __name__== "__main__":
    obj = DataIngestion()  ##calling the data ingestion class for initiating the data ingestion process
    obj.initiate_data_ingestion()  
    logging.info('class is called')



