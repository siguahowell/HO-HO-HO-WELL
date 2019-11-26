import pandas as pd
###########Loading Cars###########
cars=pd.read_csv('cars.csv')
###########Unloading first 5 and last 5 of cars.csv#############
print(cars.head(5))
print(cars.tail(5))  