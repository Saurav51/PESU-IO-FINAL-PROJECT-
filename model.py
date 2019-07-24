import pandas as pd
import numpy as np
#from datetime import datetime

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

col_names=['Date','location','mintemp','maxtemp','rainfall','evapouration','sunshine','gustdir','1','2','3','4','5','6','7','8','9','10','11','12','13','14','RainTomorrow']
    
data=pd.read_csv('dataset.csv',names=col_names)
#data.head(5)

y=data[['RainTomorrow']]
X=data.drop('RainTomorrow',axis=1)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

logreg=LogisticRegression()
logreg.fit(X_train,y_train)

y_pred=logreg.predict(X_test)
print(metrics.accuracy_score(y_pred,y_test))

"""
Created on Thu Jul 18 14:04:38 2019

@author: Saurav Nayak
"""
