# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyApp.settings')
django.setup()

# Model import
from home.models import Measurement

measurements = Measurement.objects.all() 

# Extracting features and target variable


tables = []
for m in measurements:
    payload = {'height': m.height, 'weight': m.weight, 'age': m.age, 'waist': m.waist}
    tables.append(payload)


# Extracting features and target variable
data = pd.json_normalize(tables)
X = data[['height', 'weight', 'age']]
y = data['waist']


# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)


# Predicting waist measurements for new data
new_height = 150
new_age = 50
new_weight = 80

# Reshaping the input data into a 2D array for prediction
new_data = pd.DataFrame({'height': [new_height], 'weight': [new_weight], 'age': [new_age]})
prediction = model.predict(new_data)


print("Predicted waist measurement: ", prediction[0])
