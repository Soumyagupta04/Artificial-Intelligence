import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Sample data
data = {
    'Height': [150, 160, 155, np.nan, 165, 170, 175, np.nan],
    'Weight': [50, 60, 55, 65, 70, 75, 80, 85],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60]
}
df = pd.DataFrame(data)

# Initialize the IterativeImputer
imputer = IterativeImputer(max_iter=10, random_state=0)

# Perform multiple imputation
df_imputed = imputer.fit_transform(df)

# Convert the result back to a DataFrame
df_imputed = pd.DataFrame(df_imputed, columns=df.columns)

print(df_imputed)
