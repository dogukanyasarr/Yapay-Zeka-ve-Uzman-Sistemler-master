import numpy as np
import pandas as pd
import simpsom as sps
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Veri setini yükleme
data = pd.read_csv('CC GENERAL.csv')

# Kullanılacak kolonları seçme
x = data.drop(["CUST_ID"], axis=1)

# SOM (Self-Organizing Map) ile veri kümesini önişleme
net = sps.SOMNet(20, 20, x.values, PBC=True)
net.train(train_algo="batch", start_learning_rate=0.01, epochs=10000)

# SOM çıktısını KMeans'e giriş olarak kullanma
map_data = np.array((net.project(x.values)))
kmeans = KMeans(n_clusters=3, max_iter=300, random_state=0)
kmeans.fit(map_data)

# Küme etiketlerini veri setine ekleme
data["Cluster"] = kmeans.labels_

# Her kümeye ait örnekler
print(data[data["Cluster"] == 0].head(5))
print(data[data["Cluster"] == 1].head(5))
print(data[data["Cluster"] == 2].head(5))

# Kümeleme sonuçlarını görselleştirme
labels = kmeans.labels_
centers = kmeans.cluster_centers_
plt.scatter(map_data[:, 0], map_data[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], marker='o', s=200, c='red', edgecolors='k')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('KMeans Clustering of Credit Card Customers')
plt.show()
