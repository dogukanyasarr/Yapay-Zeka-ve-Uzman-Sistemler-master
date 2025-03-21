import numpy as np
import pandas as pd
import simpsom as sps
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Veri setini oku
data = pd.read_csv('Mall_Customers.csv')  # Dosya adını kendi veri setine göre değiştir

# Kullanılacak kolonları seç
x = data[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

# SOM ağı oluştur
net = sps.SOMNet(20, 20, x.values, PBC=True)

# Eğitimi başlat
net.train(train_algo="batch", start_learning_rate=0.01, epochs=10000)

# SOM haritasını projelendir
map = np.array((net.project(x.values)))

# KMeans kümeleme
kmeans = KMeans(n_clusters=3, max_iter=300, random_state=0)
y_kmeans = kmeans.fit(map)

# Kümeleri veriye ekleyelim
data["Cluster"] = kmeans.labels_

# Kümeleri yazdır
print(data[data["Cluster"] == 0].head(5))
print(data[data["Cluster"] == 1].head(5))
print(data[data["Cluster"] == 2].head(5))

# Küme grafiği çizdirme
labels = kmeans.labels_
centers = kmeans.cluster_centers_
plt.scatter(map[:, 0], map[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], marker='o', s=200, c='red', edgecolors='k')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('KMeans Clustering - Müşteri Verisi')
plt.show()