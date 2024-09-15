import pandas as pd 
dc_listings = pd.read_csv('C:/Users/Admin/Downloads/dc_airbnb.csv')
print(dc_listings.head(1))
fist_accommadates = dc_listings.iloc[0]['accommodates']
our_accommodates = 3 
fist_distance = abs(fist_accommadates-our_accommodates)
print(fist_distance)