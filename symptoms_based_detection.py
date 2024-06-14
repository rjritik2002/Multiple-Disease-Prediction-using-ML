# -*- coding: utf-8 -*-
"""symptoms-based-detection

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16nkty6jngwC0F2e8xnn7cYrok_KREUEV
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



# loading the csv data to a Pandas DataFrame
data = pd.read_csv('symptom-based-detection.csv')

# print first 5 rows of the dataset
data.head()

# print last 5 rows of the dataset
data.tail()

# number of rows and columns in the dataset
data.shape

# getting some info about the data
data.info()

# checking for missing values
data.isnull().sum()

# statistical measures about the data
data.describe()

# checking the distribution of Target Variable
data['prognosis'].value_counts()

"""Splitting the Features and Target"""

#storing data in x and labels in y 
X = data.drop(columns='prognosis', axis=1)
Y = data['prognosis']

# printing data i.e. x
print(X)

# printing labels in y
print(Y)

"""Splitting the Data into Training data & Test Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# printing the shape of traing data and labels and testing data and labels
print(X.shape, X_train.shape, X_test.shape)

"""Model Training

# logistic regression
"""

#importing algorithm
model = LogisticRegression()

# training the LogisticRegression model with Training data
model.fit(X_train, Y_train)

"""Model Evaluation"""

# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

#printing accuracy of training data
print('Accuracy on Training data : ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# printing accuracy of testing data
print('Accuracy on Test data : ', test_data_accuracy)


import pickle
pickle.dump(model,open('symptoms_based_detection.pkl','wb'))

input_data = (1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
# std_data = scaler.transform(input_data_reshaped)
# print(std_data)

prediction = model.predict(input_data_reshaped)
print(prediction)

