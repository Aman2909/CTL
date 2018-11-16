#IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import LogisticRegression
from sklearn.cross_validation import train_test_split

dataset=pd.read_csv("LogResData.csv")

X = dataset.iloc[:,[2,3]].values
Y = dataset.iloc[:,4].values

X_train, X_test, y_train, y_test=train_test_split(X,Y,test_size=1/4,random_state=0)

