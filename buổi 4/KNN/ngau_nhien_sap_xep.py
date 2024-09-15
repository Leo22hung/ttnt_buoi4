import pandas as pd
import numpy as np 
dc_listings = pd.read_csv('C:/Users/Admin/Downloads/dc_airbnb.csv')
dc_listings['distance'] = dc_listings['accommodates'].apply(lambda x: abs(x-3))
shuffled_index = np.random.permutation(dc_listings.index)
dc_listings = dc_listings.loc[shuffled_index]
dc_listings = dc_listings.sort_values('distance')
print(dc_listings['price'].head(10))