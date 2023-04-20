import pandas as pd

df =  pd.read_csv('healthcare-dataset-stroke-data.csv')
df = df.set_index('id')