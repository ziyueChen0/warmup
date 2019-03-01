# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:41:29 2019

@author: chenz
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%hwduhd
Data = pd.read_csv("D:\OLD_D\german_credit_data.csv")
print (Data.columns)
Data.head(10)

print("Purpose : ",Data.Purpose.unique())
print("Sex : ",Data.Sex.unique())
print("Housing : ",Data.Housing.unique())
print("Saving accounts : ",Data['Saving accounts'].unique())
print("Checking account : ",Data['Checking account'].unique())

Data['Saving accounts'] = Data['Saving accounts'].map({"little":0,"moderate":1,"quite rich":2 ,"rich":3 });
Data['Saving accounts'] = Data['Saving accounts'].fillna(Data['Saving accounts'].dropna().mean())

Data['Checking account'] = Data['Checking account'].map({"little":0,"moderate":1,"rich":2 });
Data['Checking account'] = Data['Checking account'].fillna(Data['Checking account'].dropna().mean())

Data['Sex'] = Data['Sex'].map({"male":0,"female":1}).astype(float);

Data['Housing'] = Data['Housing'].map({"own":0,"free":1,"rent":2}).astype(float);

Data['Purpose'] = Data['Purpose'].map({'radio/TV':0, 'education':1, 'furniture/equipment':2, 'car':3, 'business':4,
       'domestic appliances':5, 'repairs':6, 'vacation/others':7}).astype(float);

print (Data.head(10))
plt.scatter(Data['Credit amount'],Data["Age"])
plt.figure()
sns.pairplot(Data)
plt.scatter(Data['Credit amount'],Data["Duration"])
sns.pairplot(Data)
plt.figure()
plt.scatter(Data['Saving accounts'],Data["Duration"])
plt.figure()


fig1 = Data["Job"].hist()
fig1.text(-0.5, 400, 'Frequency', ha='center')
fig1.text(0, -100, 'UnSkilled', ha='center')
fig1.text(1, -100, 'UnSkilled Resident', ha='center')
fig1.text(2, -100, 'Skilled', ha='center')
fig1.text(3, -100, 'Highly Skilled', ha='center')

