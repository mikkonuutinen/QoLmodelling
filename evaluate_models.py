# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:32:54 2021
@author: mikko.nuutinen

"""

import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, roc_auc_score
import datetime
import pickle

# create folder for analysis results
now = datetime.datetime.now()
result_dir = now.strftime('result_%Y%m%d/')
if not os.path.isdir(result_dir): os.mkdir(result_dir)

# read data (set path)
df = pd.read_pickle('D:/data/patient_data_test.pkl')

from utils import select_variables
features='selected_10'
target = 'target_M6_global_QLQ30_high'
X, y = select_variables(df, features, impution_type='none', target = 'target_M6_global_QLQ30_high')

# read model
filename = 'qol_model.sav'
clf = pickle.load(open(result_dir+filename, "rb"))




#%%

def print_scores(y_pred_proba, y_test, th=0.5):
    y_pred = (y_pred_proba[:,1] >= th).astype(bool) 
    cm=confusion_matrix(y_test, y_pred)
    auc=roc_auc_score(y_test, y_pred_proba[:,1])
    recall=recall_score(y_test, y_pred)
    precision=precision_score(y_test, y_pred)
    
    print ('\n-----------------------------------------------------------------')
    print ('\nAUC: ', auc)
    print ('Recall: ', recall)
    print ('Precision: ', precision)
    df_cm = pd.DataFrame(cm,
                      index=['NO', 'YES'],
                      columns=('PRED NO (ave)', 'PRED YES (ave)'))
    print ('\nConfusion Matrix')
    print (df_cm)


def calibration_plot(clf, X, y, save_dir, label):
    from sklearn.calibration import calibration_curve
    plt.figure(figsize=(10, 10))
    ax1 = plt.subplot2grid((3, 1), (0, 0), rowspan=2)
    ax2 = plt.subplot2grid((3, 1), (2, 0))
    
    ax1.plot([0, 1], [0, 1], "k:", label="Perfectly calibrated")
    
    prob_pos = clf.predict_proba(X)[:, 1]
    
    fraction_of_positives, mean_predicted_value = \
        calibration_curve(y, prob_pos, n_bins=10)
    
    ax1.plot(mean_predicted_value, fraction_of_positives, "s-",
             label=label)
    
    ax2.hist(prob_pos, range=(0, 1), bins=20, label=label,
             histtype="step", lw=2)
    
    ax1.set_ylabel("Fraction of positives")
    ax1.set_ylim([-0.05, 1.05])
    ax1.legend(loc="lower right")
    ax1.set_title('Calibration plots  (reliability curve)')
    
    ax2.set_xlabel("Mean predicted value")
    ax2.set_ylabel("Count")
    ax2.legend(loc="upper center", ncol=2)
    
    plt.tight_layout()
    plt.savefig(save_dir)
    
    

#%%

# AUC, recall and precision and confusion matrix, calibration plot
print ("Performance")
y_pred_proba = clf.predict_proba(X)
th=0.5
print_scores(y_pred_proba, y,th)
# lasketaan 95% luottamusvälit auc, precision, recall
import stat_util
performance = []
score, ci_lower, ci_upper, scores = stat_util.score_ci(y, y_pred_proba[:,1], score_fun=roc_auc_score)
performance.append(str(score.round(3)) + " (" + str(ci_lower.round(3)) + "-" +  str(ci_upper.round(3)) + ")")
score, ci_lower, ci_upper, scores = stat_util.score_ci(y, y_pred_proba[:,1]>th, score_fun=recall_score)
performance.append(str(score.round(3)) + " (" + str(ci_lower.round(3)) + "-" +  str(ci_upper.round(3)) + ")")
score, ci_lower, ci_upper, scores = stat_util.score_ci(y, y_pred_proba[:,1]>th, score_fun=precision_score)
performance.append(str(score.round(3)) + " (" + str(ci_lower.round(3)) + "-" +  str(ci_upper.round(3)) + ")")

print ('Performance (with ci95%):')
print ('AUC: ', performance[0])
print ('Recall: ', performance[1])
print ('Precision: ', performance[2])

# Model calibration
from sklearn.calibration import CalibratedClassifierCV
import matplotlib.pyplot as plt
calibration_plot(clf, X, y, result_dir+'training_data_calibration_plot.png', 'xgb model')














