import pandas as pd 
dc_listings = pd.read_csv('C:/Users/Admin/Downloads/dc_airbnb.csv')
dc_listings['distance'] = dc_listings['accommodates'].apply(lambda x: abs(x-3))
print(dc_listings['distance'].value_counts())