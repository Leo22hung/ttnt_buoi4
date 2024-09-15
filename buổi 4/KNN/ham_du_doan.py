import pandas as pd 
dc_listings = pd.read_csv('C:/Users/Admin/Downloads/dc_airbnb.csv')
dc_listings['price'] = dc_listings['price'].str.replace(',','').str.replace('$','').astype(float)
def predict_price(new_listing):
    temp_df = dc_listings.copy()
    temp_df['distance'] = temp_df['accommodates'].apply(lambda x: abs(x - new_listing))
    nearest_neighbors =  temp_df.sort_values('distance').head(5)
    predict_price = nearest_neighbors['price'].mean()
    return predict_price
acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)


print(f"Suggested price for 1 person: {acc_one}")
print(f"Suggested price for 2 person: {acc_two}")
print(f"Suggested price for 4 person: {acc_four}")