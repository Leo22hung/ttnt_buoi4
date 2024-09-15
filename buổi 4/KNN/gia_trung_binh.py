import pandas as pd 
dc_listings = pd.read_csv('C:/Users/Admin/Downloads/dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',','')
stripped_dollar_signs = stripped_commas.str.replace('$','')
dc_listings['price'] = stripped_dollar_signs.astype(float)
mean_price = dc_listings['price'].head(5).mean()
print(mean_price)