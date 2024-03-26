import numpy as np
import pandas as pd
import seaborn as sns
import csv

file_path = '/data/ecommerceDataset.csv'
dataset = pd.read_csv(file_path)

dataset.columns = ['Category', 'Text']
codes = {'Household':0, 'Books':1, 'Clothing & Accessories':2, 'Electronics':3}
dataset['Category_code'] = dataset['Category'].apply(lambda x: codes[x])