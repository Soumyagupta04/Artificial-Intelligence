import pandas as pd
import numpy as np

# Sample data
data = {'Color': ['Red', 'Blue', 'Red', np.nan, 'Green', 'Red']}
df = pd.DataFrame(data)

# Mode imputation
mode_value = df['Color'].mode()[0]
df['Color'].fillna(mode_value, inplace=True)

print(df)
