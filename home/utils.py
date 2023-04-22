# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Linear Regression model for waist prediction
class WaistSizePredictor:
    def __init__(self, data: list):
        self.model = LinearRegression()
        self.new_data = None
        self.data = pd.json_normalize(data)
        self.X = self.data[['height', 'weight', 'age']]
        self.y = self.data['waist']
        self.X_train, self.X_test, self.y_train, self.y_test = self.train()
        self.fit()


    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def fit(self):
        self.model.fit(self.X_train, self.y_train)

    def set_prediction_data(self, new_height, new_weight, new_age):
        self.new_data = pd.DataFrame({'height': [new_height], 'weight': [new_weight], 'age': [new_age]})

    def predict(self):
        predicted_waist = self.model.predict(self.new_data)
        return predicted_waist
