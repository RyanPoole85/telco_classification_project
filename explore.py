# standard data science imports
import pandas as pd
import numpy as np

# visualization imports
import matplotlib.pyplot as plt
import seaborn as sns

# data prep imports
from sklearn.model_selection import train_test_split

# stats import
from scipy import stats

# modeling imports
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# model evaluation imports
from sklearn.metrics import \
accuracy_score,\
recall_score,\
precision_score,\
confusion_matrix,\
classification_report

# custom modules
import env
import acquire_telco as a
import prepare as p
import explore as e


def chi2_results(observed):
    """function to print chi2 results"""
    alpha = 0.05 #setting alpha
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    print("Expected DataFrame") #print label
    print(pd.DataFrame(expected.astype('int'), index=observed.index, columns=observed.columns)) #print expected data
    print("\n") #print space
    print("Observed DataFrame") #print label
    print(observed) #print observed data
    print(f'chi^2 = {chi2:.4f}')# print the chi2 value, formatted to a float with 4 digits.
    print(f'p     = {p:.4f}')# print the p-value, formatted to a float with 4 digits.
    print('---\n')# print a new line
    if p < alpha:
        print('p is less than alpha so we reject the null hypothesis')
    else:
        print('p is higher than alpha so we fail to reject the null hypothesis')

#created function to combine data strength information since it is used multiple times.

def model_strength(y_train, y_pred):
    """function that takes in y_train and y_pred and prints useful model data"""    
    
    print(classification_report(y_train, y_pred))

    counts = pd.crosstab(y_train, y_pred)

    TP = counts.iloc[1,1]
    TN = counts.iloc[0,0]
    FP = counts.iloc[0,1]
    FN = counts.iloc[1,0]

    print(f'TP = {TP}')
    print(f'TN = {TN}')
    print(f'FP = {FP}')
    print(f'FN = {FN}')

    print(' ')

    all = (TP + TN + FP + FN)
    print(f'Total = {all}')

    print(' ')

    accuracy = (TP + TN) / all
    print(f'Accuracy = {accuracy}')

    TPR = recall = TP / (TP + FN)
    FPR = FP / (FP + TN)

    TNR = TN / (FP + TN)
    FNR = FN / (FN + TP)
    
    
    precision =  TP / (TP + FP)
    f1 =  2 * ((precision * recall) / ( precision + recall))
    print(f'Precision= {precision}')
    print(f'f1={f1}')

    print(' ')

    support_pos = TP + FN
    support_neg = FP + TN
    print(f'Support (Yes)= {support_pos}')
    print(f'Support (No)= {support_neg}')

    print(' ')
 
    print(f'True Positive Rate={TPR}')
    print(f'False Positive Rate={FPR}')
    print(f'True Negative Rate={TNR}')
    print(f'False Negative Rate={FNR}')
