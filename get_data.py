import os
import sys 
import json


from dotenv import load_dotenv

import certifi
import pandas as pd 
import numpy as np
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def pushing_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    if __name__=='__main__':
        pass


