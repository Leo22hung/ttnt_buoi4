import pandas as pd 
import numpy as np
errors_one = pd.Series([5,10,5,10,5,10,5,10,5,10,5,10,5,10,5,10,5,10])
errors_two = pd.Series([5,10,5,10,5,10,5,10,5,10,5,10,5,10,5,10,5,100])
mae_one = errors_one.mean()
rmse_one = np.sqrt((errors_one**2).mean())
print(f"MAE for errors_one: {mae_one}")
print(f"RMSE for errors_one: {rmse_one}")
mae_two = errors_two.mean()
rmse_two = np.sqrt((errors_two**2).mean())
print(f"MAE for errors_two: {mae_two}")
print(f"RMSE for errors_two: {rmse_two}")