import pandas as pd

dataframe = pd.read_csv("dataFiles/Housing.csv")

#function for step 1, just experimenting with the data file using pandas
def step1():
    print(dataframe.head(3))
    print(dataframe.tail(4))
    print(dataframe.info())
