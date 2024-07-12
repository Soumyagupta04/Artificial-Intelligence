import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

# Sample data
data = {
    'Height': [150, 160, 155, np.nan, 165, 170, 175, np.nan],
    'Weight': [50, 60, 55, 65, 70, 75, 80, 85],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60]
}
df = pd.DataFrame(data)

# Initialize the KNNImputer
imputer = KNNImputer(n_neighbors=3)

# Perform KNN imputation
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print(df_imputed)
