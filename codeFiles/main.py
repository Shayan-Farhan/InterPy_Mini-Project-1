import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("dataFiles/Housing.csv")

#function for step 1, just experimenting with the data file using pandas
def step1():
    print(dataframe.head(3))
    print(dataframe.tail(4))
    print(dataframe.info())

#sort the dataframe by year built
dataframe.sort_values('yr_built', inplace=True)


#extract data for price and years built
prices = dataframe['price']
yearsBuilt = dataframe['yr_built']

#graph price vs. square footage
fig, ax = plt.subplots()
ax.set(xlabel="Year Built", ylabel="Price", title="Price vs. Year Built")
ax.grid()
ax.plot(yearsBuilt, prices)
plt.show()