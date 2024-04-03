"""
Modular EDA Class
status: in progress
  
"""

# Import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


def read_data(path, file_type='csv'):
    if file_type == 'csv':
        return pd.read_csv(path)
    elif file_type == "excel":
        return pd.read_excel(path)
    else:
        print("File type not supported")


class EDA:
    """
      Class for Exploratory Data Analysis
    """

    def __init__(self, df):
        self.df = df

    def data_shape(self):
        return self.df.shape

    def columns_nan_count(self):
        return self.df.isna().sum()

    def duplicates_count(self):
        return self.df.duplicated().sum()

    def data_info(self):
        return self.df.info()

    def columns_unique_count(self):
        return self.df.nunique()

    def data_description(self):
        return self.df.describe()

    def n_records(self, n, head=True):
        if head == True:
            return self.df.head(n)
        else:
            return self.df.tail(n)
