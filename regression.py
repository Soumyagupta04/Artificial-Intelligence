import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
data = {
    'Height': [150, 160, 155, np.nan, 165, 170, 175, np.nan],
    'Weight': [50, 60, 55, 65, 70, 75, 80, 85],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60]
}
df = pd.DataFrame(data)

# Separate data into complete cases and missing cases
complete_cases = df.dropna(subset=['Height'])
missing_cases = df[df['Height'].isna()]

# Prepare the training and prediction sets
X_train = complete_cases.drop(columns=['Height'])
y_train = complete_cases['Height']
X_pred = missing_cases.drop(columns=['Height'])

# Train the regression model
reg = LinearRegression()
reg.fit(X_train, y_train)

# Predict the missing values
y_pred = reg.predict(X_pred)

# Impute the missing values
df.loc[df['Height'].isna(), 'Height'] = y_pred

print(df)
