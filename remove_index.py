import pandas as pd

file = pd.read_csv('./data/merged_results.csv')

file = file.drop('Unnamed: 0', axis=1)

file.to_csv('./data/merged.csv')


