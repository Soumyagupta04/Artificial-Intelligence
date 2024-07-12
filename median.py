import pandas as pd
import numpy as np

# Sample data
data = {'Height': [150, 160, 155, np.nan, 165]}
df = pd.DataFrame(data)

# Median imputation
median_value = df['Height'].median()
df['Height'].fillna(median_value, inplace=True)

print(df)
