## Differentiating signals from noise

from sklearn import svm
from sklearn.externals import joblib

#SN_measurements = pickle.load(open("SN_data", 'r'))
SN_measurements_data   = [[4,5,6], [1,2,3], [7,8,9], [0,0,0], [10,10,10]]
SN_measurements_target = [True, True, False, True, False] 

SN = svm.SVC()
X  = SN_measurements_data
y  = SN_measurements_target
SN.fit(X, y)

joblib.dump(SN, 'signal_svm.pkl')

