import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn import datasets
from sklearn.metrics.cluster import fowlkes_mallows_score

# importing scikit-learn's handwritten digits dataset
digits = datasets.load_digits()
X      = digits.data
y      = digits.target


# K-Means clustering
from sklearn.cluster import KMeans

k_clus    = KMeans(n_clusters=10)
k_labels  = k_clus.fit(X).labels_
k_cm      = confusion_matrix(y, k_labels)
k_fms     = fowlkes_mallows_score(y, k_labels)

# Agglomerative clustering with ward linkage
from sklearn.cluster import AgglomerativeClustering as Agg

agg_clus    = Agg(linkage='ward', n_clusters=10)
agg_labels  = agg_clus.fit(X).labels_
agg_cm      = confusion_matrix(y, agg_labels)
agg_fms     = fowlkes_mallows_score(y, agg_labels)

# Affinity propagation
from sklearn.cluster import AffinityPropagation as Aff

preference  = -50000
aff_clus    = Aff(preference=preference)
aff_labels  = aff_clus.fit(X).labels_
aff_cm      = confusion_matrix(y, aff_labels)
aff_fms     = fowlkes_mallows_score(y, aff_labels)


# printing out results
print("K-means clustering confusion matrix:")
print(k_cm)
print("Cluster labels according to majority population:", k_cm.argmax(axis=0))
#print(k_cm.argmax(axis=0))
print("---------------------------------------------------------------------")

print("Agglomerative clustering confusion matrix:")
print(agg_cm)
print("Cluster labels according to majority population:", agg_cm.argmax(axis=0))
#print(agg_cm.argmax(axis=0))
print("---------------------------------------------------------------------")

print("Affinity Propagation clustering confusion matrix:")
print(aff_cm)
print("Cluster labels according to majority population:", aff_cm.argmax(axis=0))
#print(aff_cm.argmax(axis=0))
print("---------------------------------------------------------------------")

print("K-Means clustering Fowlkes and Mallows index               :", k_fms)
print("Agglomerative clustering Fowlkes and Mallows index         :", agg_fms)
print("Affinity Propagation clustering Fowlkes and Mallows index  :", aff_fms)
