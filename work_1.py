import pandas as pd 
Melb_data_fe = pd.read_csv('data/melb_data_fe.csv', sep= ',')
fe = Melb_data_fe.copy()
fe.head()