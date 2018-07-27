# Differentiating QPSK from the rest

from sklearn import svm
from sklearn.externals import joblib

#QPSK_measurement = pickle.load(open("QPSK_data", 'r'))
QPSK_measurements_data   = [[11, 12, 10], [44, 56, 41], [99, 100, 101]]
QPSK_measurements_target = [True, False, False]

Q = svm.SVC()
X = QPSK_measurements_data
y = QPSK_measurements_target
Q.fit(X, y)

joblib.dump(Q, 'qpsk_svm.pkl')
