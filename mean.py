import pandas as pd
import numpy as np

# Sample data
data = {'Height': [150, 160, 155, np.nan, 165]}
df = pd.DataFrame(data)

# Mean imputation
mean_value = df['Height'].mean()
df['Height'].fillna(mean_value, inplace=True)

print(df)
