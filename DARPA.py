import numpy as np
from sklearn import svm
from sklearn.externals import joblib

# Labels
#    1 -- QPSK
#    2 -- GMSK
#    3 -- FMSK
#    4 -- unidentifiable

class Categorize():

    def __init__(self):
       self.signal_svm = joblib.load('signal_svm.pkl')
       self.qpsk_svm   = joblib.load('qpsk_svm.pkl')
       self.gmsk_svm   = joblib.load('gmsk_svm.pkl')
       self.fmsk_svm   = joblib.load('fmsk_svm.pkl')

    def classify(self,data):
        label = 4

        if self.signal_svm.predict(data) == True:
            if self.qpsk_svm.predict(data) == True:
                label = 1
            elif self.gmsk_svm.predict(data) == True:
                label = 2
            elif self.fmsk_svm.predict(data) == True:
                label = 3

        return label



clf  = Categorize()

#file = pickle.load("readings", 'r')
file = [11,45,67]
L    = clf.classify(file)

if L == 1:
    print('QPSK')
elif L == 2:
    print('GMSK')
elif L == 3:
    print('FMSK')
elif L == 4:
    print('Sorry! Could not identify it.')

