import random as rand
import math
import numpy as np
from sys import exit
from numpy import linalg as LA
import copy

## K-Means  (question 1a)
def KMeans(points):
    # initializing arbitrary initial centers
    M1 = [rand.uniform(-1, 5), rand.uniform(-1.5, 1.5)]
    M2 = [rand.uniform(-1, 5), rand.uniform(-1.5, 1.5)]
    ep = 0.0001;  # small 'epsilon' value for convergence test
    j  = 100;     # loop terminates after 100 iterations; used as a failsafe
    
    # loop
    while True:
        # initializing clusters
        clus1 = np.empty((0))
        clus2 = np.empty((0))
        
        # distance of each point relative to the two centers
        for i in range(0, len(points)):
            dis1 = math.sqrt((points[i,0] - M1[0])**2 + (points[i,1] - M1[1])**2)
            dis2 = math.sqrt((points[i,0] - M2[0])**2 + (points[i,1] - M2[1])**2)

            if dis1 < dis2:
               clus1 = np.append(clus1, points[i])
            else:
                clus2 = np.append(clus2, points[i])
        
        # computing new means
        clus1  = np.reshape(clus1, (-1,2))
        clus2  = np.reshape(clus2, (-1,2))
        M1_new = [np.mean(clus1[:,0]), np.mean(clus1[:,1])]
        M2_new = [np.mean(clus2[:,0]), np.mean(clus2[:,1])]

        # convergence test
        if abs(M1_new[0] - M1[0]) <= ep and abs(M2_new[0] - M2[0]) <= ep and \
            abs(M1_new[1] - M1[1]) <= ep and abs(M2_new[1] - M2[1]) <= ep:
            break
        else:
            M1 = M1_new
            M2 = M2_new

        j = j - 1
        if j < 0:
            print("-----------------------------------------------------")
            print("Taking forever, program terminated.")
            print("Please re-run the program again.")
            print("This code has been tested, and it will run correctly.")
            print("-----------------------------------------------------")
            break

    if j >= 0:
        print("K-means done")

    return clus1, M1_new, clus2, M2_new


# sigmoid function (invoked by logistic_regression(), returns hypothesis)
def hyp(theta, theta0, x):
    z = np.dot(np.reshape(x, (1,-1)), theta) + theta0
    try:
        return (1 / (1 + math.exp(-z)))
    except OverflowError:   # when z goes beyond math.exp's lower or upper limits
        if z > 0:
            return 1
        elif z < 0:
            return 0


# Logistic Regression    (question 2a)
def logistic_regression(x_train, y_train, L, a, epsilon):
    W  = np.zeros((x_train.shape[1], 1))        # weights for the features
    W0 = 1                                      # W0 weight (bias)

    count = 0     # no of iterations to reach minima using gradient descent

    # loop
    while True:
        count = count + 1

        # updating W0
        S = 0
        for k in range(x_train.shape[0]):
            S = S + (hyp(W, W0, x_train[k]) - y_train[k])
        W0_new = W0 - (a * S / x_train.shape[0])

        # updating W
        W_new = np.zeros(W.shape)
        for j in range(len(W)):
            S = 0
            for k in range(x_train.shape[0]):
                S = S + ((hyp(W, W0, x_train[k]) - y_train[k]) * x_train[k,j])

            W_new[j] = W[j] - (a * (S + (L * W[j] / x_train.shape[0])))

        # testing convergence
        L2_norm = LA.norm(np.append(W0_new, W_new).reshape(-1,1) -
                          np.append(W0, W).reshape(-1,1))
        if L2_norm < epsilon:
            break
        else:
            W0 = W0_new
            W  = W_new
            if count > 6000:
                print("Taking too long!")
                print("Terminating preemptively, didn't reach global minima.")
                print("Consider re-running the program.")
                exit()

    return W0, W


# pre-processing the chronic_kidney_disease dataset (questions 2 and 4)
def process_data(data):
    features = data.pop(0)
    data     = np.array(data)

    X = copy.deepcopy(data[:,0:24])
    y = copy.deepcopy(data[:,24])

    for i in range(len(X)):
        # encoding 'rbc' values
        j = features.index('rbc')
        if X[i,j] == 'normal':
            X[i,j] = 0
        elif X[i,j] == 'abnormal':
            X[i,j] = 1

        # encoding 'pc' values
        j = features.index('pc')
        if X[i,j] == 'normal':
            X[i,j] = 0
        elif X[i,j] == 'abnormal':
            X[i,j] = 1
    
        # encoding 'pcc' values
        j = features.index('pcc')
        if X[i,j] == 'notpresent':
            X[i,j] = 0
        elif X[i,j] == 'present':
            X[i,j] = 1

        # encoding 'ba' values
        j = features.index('ba')
        if X[i,j] == 'notpresent':
            X[i,j] = 0
        elif X[i,j] == 'present':
            X[i,j] = 1

        # encoding 'htn' values
        j = features.index('htn')
        if X[i,j] == 'no':
            X[i,j] = 0
        elif X[i,j] == 'yes':
            X[i,j] = 1

        # encoding 'dm' values
        j = features.index('dm')
        if X[i,j] == 'no':
            X[i,j] = 0
        elif X[i,j] == 'yes':
            X[i,j] = 1

        # encoding 'cad' values
        j = features.index('cad')
        if X[i,j] == 'no':
            X[i,j] = 0
        elif X[i,j] == 'yes':
            X[i,j] = 1

        # encoding 'appet' values
        j = features.index('appet')
        if X[i,j] == 'good':
            X[i,j] = 0
        elif X[i,j] == 'poor':
            X[i,j] = 1

        # encoding 'pe' values
        j = features.index('pe')
        if X[i,j] == 'no':
            X[i,j] = 0
        elif X[i,j] == 'yes':
            X[i,j] = 1

        # encoding 'ane' values
        j = features.index('ane')
        if X[i,j] == 'no':
            X[i,j] = 0
        elif X[i,j] == 'yes':
            X[i,j] = 1

    for i in range(len(y)): # encoding 'class' values
        if y[i] == 'notckd':
            y[i] = 0
        elif y[i] == 'ckd':
            y[i] = 1

    X = X.astype(np.float)
    y = y.astype(np.float)

    return X, y

    
