import csv
import numpy as np
import matplotlib.pyplot as plt
from HW4 import logistic_regression, hyp, process_data

## importing contents of the csv file (missing values filled in using WEKA)
f = open('chronic_kidney_disease_full.csv')
file = csv.reader(f)

data = []
for row in file:
    data.append(row)
    
f.close()


## pre-processing the data
X, y = process_data(data)   # X : features, y : class


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

## Logistic regression
lamb = np.array([-2, -1.8, -1.6, -1.4, -1.2,
                 -1, -0.8, -0.6, -0.4, -0.2,
                 0, 0.2, 0.4, 0.6, 0.8,
                 1, 1.2, 1.4, 1.6, 1.8,
                 2, 2.2, 2.4, 2.6, 2.8,
                 3, 3.2, 3.4, 3.6, 3.8, 4])
alpha = 0.0000001                           # learning rate
ep    = 0.001                               # epsilon for convergence test

from sklearn.metrics import f1_score
F = np.empty((0))   # stores f-measures for different lambdas

# predicts test set instances and returns f_measure
def f_measure(y_true, x_test, w, w0):
    y_pred = np.empty((0))
    for z in range(x_test.shape[0]):
        if hyp(w, w0, x_test[z]) > 0.5:
            y_pred = np.append(y_pred, 1)
        else:
            y_pred = np.append(y_pred, 0)

    return f1_score(y_true, y_pred)
    
print("Learning rate alpha =", alpha)


# performing logistic regression and calculating f-measure
for l in range(len(lamb)):
    L = lamb[l]     # regularization parameter lambda
    print("Current lambda value =", L)

    W0, W = logistic_regression(X_training, y_training, L, alpha, ep)
    
    # Weights set; predicting on test data
    F = np.append(F, f_measure(y_test, X_test, W, W0))


# plotting f-measure vs. regularization parameter
plt.figure()
plt.plot(lamb, F, 'ro')
plt.ylabel('f - measure')
plt.xlabel('Regularization parameter $\lambda$')
plt.grid()
plt.axis([-3, 5, 0.7, 0.85])
plt.title('Answer 2(b)')
plt.show()
