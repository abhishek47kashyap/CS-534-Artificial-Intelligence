# Differentiating FMSK from the rest

from sklearn import svm
from sklearn.externals import joblib

#FMSK_measurement = pickle.load(open("FMSK_data", 'r'))
FMSK_measurements_data   = [[11, 12, 13], [44, 56, 59], [99, 100, 89]]
FMSK_measurements_target = [False, False, True]

F = svm.SVC()
X = FMSK_measurements_data
y = FMSK_measurements_target
F.fit(X, y)

joblib.dump(F, 'fmsk_svm.pkl')
