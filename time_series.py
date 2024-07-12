import pandas as pd
import numpy as np

# Create a date range
dates = pd.date_range('20230101', periods=10)

# Create a DataFrame with missing values
data = {
    'Date': dates,
    'Value': [1.0, np.nan, 3.0, np.nan, 5.0, np.nan, 7.0, 8.0, np.nan, 10.0]
}
df = pd.DataFrame(data).set_index('Date')

print("Original DataFrame with Missing Values:")
print(df)

# Forward fill imputation
df_ffill = df.fillna(method='ffill')
print("\nForward Fill Imputation:")
print(df_ffill)

# Backward fill imputation
df_bfill = df.fillna(method='bfill')
print("\nBackward Fill Imputation:")
print(df_bfill)

# Linear interpolation imputation
df_interpolated = df.interpolate(method='linear')
print("\nLinear Interpolation Imputation:")
print(df_interpolated)

# Cubic spline interpolation imputation
df_cubic = df.interpolate(method='spline', order=3)
print("\nCubic Spline Interpolation Imputation:")
print(df_cubic)
