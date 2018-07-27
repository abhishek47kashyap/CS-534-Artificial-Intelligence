import csv
import numpy as np
from HW4 import process_data

## importing contents of the csv file (missing values filled in using WEKA)
f = open('chronic_kidney_disease_full.csv')
file = csv.reader(f)

data = []
for row in file:
    data.append(row)
    
f.close()


## pre-processing the data
X, y = process_data(data)


## preparing training and test sets
from sklearn.model_selection import train_test_split as tts

# selecting instances from class 'ckd'
XX = X[0:250]
yy = y[0:250]
X_tr_ckd, X_ts_ckd, y_tr_ckd, y_ts_ckd = tts(XX, yy, test_size=0.2)

# selecting instances from class 'notckd'
XX = X[250:400]
yy = y[250:400]
X_tr_nckd, X_ts_nckd, y_tr_nckd, y_ts_nckd = tts(XX, yy, test_size=0.2)

# putting together training and test sets
X_training = np.vstack((X_tr_ckd, X_tr_nckd))
y_training = np.append(y_tr_ckd, y_tr_nckd)
X_test     = np.vstack((X_ts_ckd, X_ts_nckd))
y_test     = np.append(y_ts_ckd, y_ts_nckd)


## performing classification
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier as RFC

def f_measure(y_true, x_test, clf):
    # predicts test set instances and returns f_measure
    y_pred = np.empty((0))
    for i in range(len(x_test)):
        y_pred = np.append(y_pred, clf.predict(np.reshape(x_test[i], (1,-1))))

    return f1_score(y_true, y_pred)
    
# SVM with 'linear' kernel
svm_linear = SVC(kernel='linear')
svm_linear.fit(X_training, y_training)
F_linear = f_measure(y_test, X_test, svm_linear)
print("F-measure for SVM with linear kernel =", F_linear)

# SVM with 'rbf' kernel
svm_rbf = SVC(kernel='rbf')
svm_rbf.fit(X_training, y_training)
F_rbf = f_measure(y_test, X_test, svm_rbf)
print("F-measure for SVM with rbf kernel    =", F_rbf)

# Random Forest
rfc = RFC()
rfc.fit(X_training, y_training)
F_rfc = f_measure(y_test, X_test, rfc)
print("F-measure for RandomForestClassifier =", F_rfc)
