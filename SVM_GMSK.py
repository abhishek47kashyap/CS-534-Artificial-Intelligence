# Differentiating GMSK from the rest

from sklearn import svm
from sklearn.externals import joblib

#GMSK_measurement = pickle.load(open("GMSK_data", 'r'))
GMSK_measurements_data   = [[11, 12, 13], [44, 56, 61], [99, 100, 101]]
GMSK_measurements_target = [False, False, True]

G = svm.SVC()
X = GMSK_measurements_data
y = GMSK_measurements_target
G.fit(X, y)

joblib.dump(G, 'gmsk_svm.pkl')
