import numpy as np
import pandas as pd

data = pd.read_csv("C:\Users\admin\Desktop\KLASÖRLER\üniversite\4. sınıf 2. dönem\Yapay Zeka ve Uzman Sistemler\Uygulama 4\train.csv")

from sklearn.preprocessing import LabelEncoder
label_enconder = LabelEncoder().fit(data.price_range)
labels = label_enconder.transform(data.price_range)
classes = list(label_enconder.classes_)

x = data.drop("price_range", axis=1)
y = labels

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X = sc.fit_transform(x)