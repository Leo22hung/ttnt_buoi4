import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
dc_listings = pd.read_csv('C:/Users/Admin/Downloads/dc_airbnb.csv')
dc_listings['price'] = dc_listings['price'].str.replace(',','').str.replace('$','').astype(float)
train_df, test_df = train_test_split(dc_listings, test_size=0.25, random_state=42)

def predict_price(new_listing):
    temp_df = dc_listings.copy()
    temp_df['distance'] = temp_df['accommodates'].apply(lambda x: abs(x - new_listing))
    nearest_neighbors =  temp_df.sort_values('distance').head(5)
    predicted_price = nearest_neighbors['price'].mean()
    return predicted_price
test_df['predicted_price'] = test_df['accommodates'].apply(predict_price)
print(test_df[['accommodates','price','predicted_price']].head())
mae = np.mean(np.absolute(test_df['price']-test_df['predicted_price']))
mse = np.mean((test_df['price']-test_df['predicted_price'])**2)
print(f"Mean Absolute Error (MAE):{mae}")
print(f"Mean Squared Error (MSE): {mse}")
