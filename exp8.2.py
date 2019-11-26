import pandas as pd
###########Loading Cars###########
cars=pd.read_csv('cars.csv')
print(cars.iloc[0:5,0:12:2])
print(cars.loc[cars['Model']=='Mazda RX4'])
print(cars.loc[cars['Model']=='Camaro Z28']['cyl'])
#####for MazdaRX4#################################
print('%------------------------------Mazda RX4 Wag-------------------------------%')
print(cars.loc[cars.Model=='Mazda RX4 Wag']['cyl'])
print(cars.loc[cars.Model=='Mazda RX4 Wag']['gear'])
#############for Ford Panthera L############
print('%-----------------------------Ford Pantera L--------------------------------%')
print(cars.loc[cars.Model=='Ford Pantera L']['cyl'])
print(cars.loc[cars.Model=='Ford Pantera L']['gear'])
##################for Honda Civic##################
print('%--------------------------------Honda Civic-------------------------------%')
print(cars.loc[cars.Model=='Honda Civic']['cyl'])
print(cars.loc[cars.Model=='Honda Civic']['gear'])
