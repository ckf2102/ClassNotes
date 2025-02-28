# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 20:40:14 2015

@author: Corinne
"""

"""
Read titanic.csv into a DataFrame.
Define Pclass and Parch as the features, and Survived as the response.
Split the data into training and testing sets.
Fit a logistic regression model and examine the coefficients to confirm that they make intuitive sense.
Make predictions on the testing set and calculate the accuracy.
Bonus: Compare your testing accuracy to the "null accuracy", a term we've seen once before.
Bonus: Add Age as a feature, and calculate the testing accuracy. There will be a small issue you'll have to deal with.
"""

import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT7/master/data/titanic.csv')

feature_cols = ['Pclass', 'Parch']
X = data[feature_cols]
y = data.Survived

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

logreg = LogisticRegression(C=1e9)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

logreg.fit(X_train,y_train)

print logreg.intercept_
zip(feature_cols, logreg.coef_[0])

y_pred_class = logreg.predict(X_test)
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred_class)