import numpy as np
import pandas as pd
import simpsom as sps
from sklearn.cluster import KMeans

data = pd.read_csv('/content/Airline Safety.csv')

x = data.drop(["airline", "avail_seat_km_per_week"], axis=1)

net = sps.SOMNet(20, 20, x.values, PBC=True)

net.train(train_algo="batch", start_learning_rate=0.01, epochs=10000)

map = np.array((net.project(x.values)))
kmeans = KMeans(n_clusters=3, max_iter=300, random_state=0)

y_ort = kmeans.fit(map)

data["Labels"] = kmeans.labels_

print(data[data["Labels"] == 0].head(5))

print(data[data["Labels"] == 1].head(5))

print(data[data["Labels"] == 2].head(5))

import matplotlib.pyplot as plt

labels = kmeans.labels_
centers = kmeans.cluster_centers_
plt.scatter(map[:, 0],map[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], marker='o', s=200, c='red', edgecolors='k')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('KMeans CLustering')
plt.show()