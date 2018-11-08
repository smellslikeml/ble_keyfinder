#!/usr/bin/env python
import pickle
import numpy as np
import pandas as pd
import xgboost as xgb
from ast import literal_eval
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix

with open('bt_logs.txt', 'r') as infile:
    data = infile.readlines()
    
data = [literal_eval(d.strip()) for d in data]
df = pd.DataFrame(data)
df = df.replace({'0': np.nan})
df = df.sample(frac=1).reset_index(drop=True)

N = 4 * df.shape[0] // 5
test = df[N:]
train = df[:N]

label = train.pop('location').values
train = train.values

lbls = test.pop('location').values
num_class = len(list(set(lbls)))
test = test.values

clf = XGBClassifier(max_depth=4, 
                    learning_rate=0.05, 
                    n_estimators=300, 
                    objective='multi:softmax', 
                    n_jobs=4, 
                    num_class=num_class)
preds = clf.fit(train, label).predict(test)
s = pickle.dump(clf, 
                open('bt_model.dat', 'wb'), 
                protocol=2)

pred_lbl = list(zip(preds, lbls))
print(pred_lbl)
print(confusion_matrix(lbls, preds))
xgb.plot_importance(clf)
plt.show()
