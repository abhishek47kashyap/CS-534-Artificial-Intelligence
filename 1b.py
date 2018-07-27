import numpy as np
import matplotlib.pyplot as plt
import random as rand
import math
from HW4 import KMeans 

## importing .txt file
data = np.loadtxt('realdata.txt', dtype='float')
data = np.delete(np.array(data), 0, axis=1)

## performing K-means clustering
[cluster1, center1, cluster2, center2] = KMeans(data)
print("Center of cluster 1 is at :", center1)
print("No. of points in cluster 1 :", len(cluster1))
print("Center of cluster 2 is at :", center2)
print("No. of points in cluster 2 :", len(cluster2))

## plotting data
plt.figure()
plt.subplot(1,2,1)
plt.title('Points before clustering')
plt.xlabel('Length')
plt.ylabel('Width')
plt.scatter(data[:,0], data[:,1], s=4)  # obviously, there are 2 clusters

plt.subplot(1,2,2)
plt.title('Points after clustering')
plt.xlabel('Length')
plt.ylabel('Width')
plt.scatter(cluster1[:,0], cluster1[:,1], color='red', s=4, label='Cluster 1')
plt.scatter(cluster2[:,0], cluster2[:,1], color='blue', s=4, label='Cluster 2')
plt.scatter(center1[0], center1[1], marker="x", s=150, color='red', linewidths=6)
plt.scatter(center2[0], center2[1], marker="x", s=150, color='blue', linewidths=6)
plt.legend()
plt.show()
