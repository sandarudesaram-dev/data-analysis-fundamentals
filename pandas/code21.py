# EXERCISE: SELECTION

'''
Ask user for a Pokemon name and output its details if exist, otherwise raise a KeyError
'''

import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")

pokemon = input("Enter a Pokemon Name: ")

try:
	print(df.loc[pokemon])
except KeyError:
	print(f"{pokemon} not found")