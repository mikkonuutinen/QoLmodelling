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
df = pd.read_pickle('D:/data/pata_data_v2.pkl')


#%%



# SFS logistic regression variable selection
def sfs_lr(features, target, df, impution_type, th):
    from sklearn import linear_model
    import numpy as np
    from mlxtend.feature_selection import SequentialFeatureSelector as SFS
    from utils import select_variables
    df_sel_x, df_sel_y = select_variables(df,features,impution_type,target)

    variables=list(df_sel_x.columns)
    # Data normalization
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    scaler.fit(df_sel_x)
    df_sel_x = pd.DataFrame(scaler.transform(df_sel_x))
    df_sel_x.columns = variables
    seed = 10            
    clf = linear_model.LogisticRegression()

    df_variables = pd.DataFrame()
    df_auc_train = pd.DataFrame()
    df_auc = pd.DataFrame()
    iterations = 10
    for k in range(iterations):
        
        X_train, X_test, y_train, y_test = train_test_split(df_sel_x, df_sel_y, test_size=0.2, random_state=seed+k, stratify=df_sel_y)
                
        features_amount = 10
        sfs = SFS(clf,
                  k_features=features_amount, 
                  forward=True, 
                  floating=False, 
                  scoring='roc_auc', 
                  cv=10)
        sfs = sfs.fit(X_train, y_train)    
        sfs_df = pd.DataFrame.from_dict(sfs.get_metric_dict()).T
        
        auc_train=[]
        for cc in range(1,features_amount+1):
            auc_train.append(sfs_df['cv_scores'][cc].mean())
        
        feature_order=[]
        feature_order.append(sfs_df['feature_idx'][1][0])
        for aa in range(1,features_amount): 
            a=list(sfs_df['feature_idx'][aa])
            b=list(sfs_df['feature_idx'][aa+1])
            for k1 in range (len(a)):
                for k2 in range (len(b)-1,-1,-1):
                    if (a[k1] == b[k2]):
                        b.remove(a[k1])
            feature_order.append(b[0])
        
        vars_selected = []
        print ('\nMax Mean AUC: ' + str(sfs_df['avg_score'][features_amount]))
        for bb in range(features_amount):
            vars_selected.append(variables[feature_order[bb]]) 

        # SFS scores for test data set
        auc=[]
        recall=[]
        precision=[]
        for aa in range(1,features_amount+1):
            vars_selected_temp = vars_selected[:aa]
            X=np.array(X_train[vars_selected_temp])
            y=np.array(y_train).reshape((len(y_train), 1))
            clf.fit(X,y)
            
            x_test=np.array(X_test[vars_selected_temp])
            y_test=np.array(y_test).reshape((len(y_test), 1))
            y_pred = (clf.predict_proba(x_test)[:,1] >= th).astype(bool) 
            y_pred_proba = clf.predict_proba(x_test)
            auc.append(roc_auc_score(y_test, y_pred_proba[:,1]))
            recall.append(recall_score(y_test, y_pred))
            precision.append(precision_score(y_test, y_pred))

        df_variables['variables_'+str(k)] = vars_selected_temp
        df_auc['auc_'+str(k)] = auc
        df_auc_train['auc_train_'+str(k)] = auc_train
        
    return df_auc_train, df_auc, df_variables


# RF classifier grid search
def rf_grid_search(features, target, x_train, y_train):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import GridSearchCV
    from utils import select_variables
    
    seed = 10    

    clf = RandomForestClassifier()
    
    param_grid = {
            'max_depth': [2, 3, 4, 6, 8],
            'min_samples_leaf': [1, 2, 3, 4],
            'min_samples_split': [1, 2, 3, 4],
            'n_estimators': [20, 25, 30, 35, 40]}
        
    clf = GridSearchCV(estimator=clf,
             param_grid=param_grid)

    clf.fit(x_train, y_train)
    
    best_score = clf.best_score_
    best_params = clf.best_params_
    print("Best score: {}".format(best_score))
    print("Best params: ")
    for param_name in sorted(best_params.keys()):
        print('%s: %r' % (param_name, best_params[param_name]))
    
    clf_best = clf.best_estimator_
    clf_best.fit(x_train, y_train)
    
 
    return clf_best




#%%
#------------------------------------------------------------------------------
# STEP 1. Variable selection
# What are ten best features from different groups?

features='sode'
target = 'target_M6_global_QLQ30_high'
df_results_sfs_train_sode, df_results_sfs_sode, df_sfs_variables_sode = sfs_lr(features, target, df.copy(), impution_type='none',th=0.5)   

features='scales'
target = 'target_M6_global_QLQ30_high'
df_results_sfs_train_scales, df_results_sfs_scales, df_sfs_variables_scales = sfs_lr(features, target, df.copy(), impution_type='none',th=0.5)   

features = 'all_raw_m0'
target = 'target_M6_global_QLQ30_high'
df_results_sfs_train_raw, df_results_sfs_raw, df_sfs_variables_raw = sfs_lr(features, target, df.copy(), impution_type='none',th=0.5)  

features = 'medical'
target = 'target_M6_global_QLQ30_high'
df_results_sfs_train_raw, df_results_sfs_raw, df_sfs_variables_raw = sfs_lr(features, target, df.copy(), impution_type='none',th=0.5)  


#%%
#------------------------------------------------------------------------------
# STEP 2. Hyperparameter searching & Model training
from utils import select_variables
features='selected_10'
target = 'target_M6_global_QLQ30_high'
df_sel_x, df_sel_y = select_variables(df, features, impution_type='none', target = 'target_M6_global_QLQ30_high')
y = df_sel_y[target]
X = df_sel_x
seed = 10

# train/test 80%/20%
#x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed, stratify=y)

# train all data (->calculate train data performance values)
y_train = df_sel_y[target]
x_train = df_sel_x
y_test = df_sel_y[target]
x_test = df_sel_x

clf_best = rf_grid_search(features, target, x_train, y_train) # train xgb model

y_pred = (clf_best.predict_proba(x_test)[:,1] >= 0.5).astype(bool) 
y_pred_proba = clf_best.predict_proba(x_test)
cm=confusion_matrix(y_test, y_pred)
auc=roc_auc_score(y_test, y_pred_proba[:,1])
recall=recall_score(y_test, y_pred)
precision=precision_score(y_test, y_pred)

df_cm = pd.DataFrame(cm,
                  index=['NO', 'YES'],
                  columns=('PRED NO (ave)', 'PRED YES (ave)'))
feature_importances = pd.DataFrame(index=list(x_train.columns))
feature_importances['value'] =  clf_best.feature_importances_.tolist()

print ('\n-----------------------------------------------------------------')
print ('Prediction: ' + target)
print ('RF model with ' + features +' features and grid-searched hyperparameters (HUS test set)')
print ('\n',clf_best)
print ('\nAUC: ', auc)
print ('Recall: ', recall)
print ('Precision: ', precision)

print ('\nConfusion Matrix')
print (df_cm)

print ('\nFeature importances (ten highest):')
print (feature_importances.T.mean().sort_values(ascending=False)[:10])


filename = 'qol_model.sav'
pickle.dump(clf_best, open(result_dir+filename, 'wb'))












