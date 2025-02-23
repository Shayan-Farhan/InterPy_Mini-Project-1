import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("dataFiles/Housing.csv")

#function for step 1, just experimenting with the data file using pandas
def step1():
    print(dataframe.head(3))
    print(dataframe.tail(4))
    print(dataframe.info())

#function for taking a 2Dlist, and returning a list with the average of each row

#sort the dataframe by year built
dataframe.sort_values('yr_built', inplace=True)

#extract data for price and years built
housesByDecade = [dataframe[(dataframe['yr_built'] >= 1900) & (dataframe['yr_built'] < 1910)],
                  dataframe[(dataframe['yr_built'] >= 1910) & (dataframe['yr_built'] < 1920)],
                  dataframe[(dataframe['yr_built'] >= 1920) & (dataframe['yr_built'] < 1930)],
                  dataframe[(dataframe['yr_built'] >= 1930) & (dataframe['yr_built'] < 1940)],
                  dataframe[(dataframe['yr_built'] >= 1940) & (dataframe['yr_built'] < 1950)],
                  dataframe[(dataframe['yr_built'] >= 1950) & (dataframe['yr_built'] < 1960)],
                  dataframe[(dataframe['yr_built'] >= 1960) & (dataframe['yr_built'] < 1970)],
                  dataframe[(dataframe['yr_built'] >= 1970) & (dataframe['yr_built'] < 1980)],
                  dataframe[(dataframe['yr_built'] >= 1980) & (dataframe['yr_built'] < 1990)],
                  dataframe[(dataframe['yr_built'] >= 1990) & (dataframe['yr_built'] < 2000)],
                  dataframe[(dataframe['yr_built'] >= 2000) & (dataframe['yr_built'] < 2010)],
                  dataframe[dataframe['yr_built'] >= 2010]
                  ]

pricesByDecade = []
for i in range(len(housesByDecade)):
    pricesByDecade.append(housesByDecade[i]['price'])

averagePriceByDecade = []
for i in range(len(pricesByDecade)):
    averagePriceByDecade.append(int(pricesByDecade[i].mean()))

decades = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]



"""graph bar chart of price vs. year built
fig, ax = plt.subplots()
ax.set(xlabel="Year Built", ylabel="Price", title="Price vs. Year Built")
ax.grid()
ax.plot(yearsBuilt, prices)
#plt.show()
"""