#!/usr/bin/env python
# coding: utf-8

# In[31]:


from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

data =fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
print("First 10 rows of the dataset:")
print(df.head(10))
print("\nBasic statistics for each feature:")
print(df.describe())
missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)
df.fillna(df.mean())
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

LReg =LinearRegression()
LReg.fit(X_train_scaled, y_train)
y_pred = LReg.predict(X_test_scaled)
print(y_pred)
RReg =Ridge()
RReg.fit(X_train_scaled, y_train)
y_pred = RReg.predict(X_test_scaled)
print(y_pred)


# In[ ]:





# In[ ]:





# In[ ]:




