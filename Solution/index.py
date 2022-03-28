from sklearn.cluster import KMeans
import numpy as np
with open('BROADCAST\input10.txt') as f:
    n, k = [int(x) for x in next(f).split()]
    X = []
    for line in f:
        X.append([int(x) for x in line.split()])
kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
kmeans.labels_
# kmeans.predict(X[0], X[1])
kmeans.cluster_centers_
print(kmeans.cluster_centers_)
with open("output10.txt", "w") as external_file:
    print(k, file=external_file)
    for i in kmeans.cluster_centers_:
        print("{:.6f}".format(i[0]), "{:.6f}".format(i[1]), file=external_file)
    external_file.close()
