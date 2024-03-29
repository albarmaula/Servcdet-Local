# Import library Scikit-Learn
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler 
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# Load data
df = np.asarray(pd.read_csv("ResNet50_output/data2classherlev1.csv", header=None))

# Pisahkan fitur dan target dari dataset
X = df[:, 0:-1]
y = df[:, -1][np.newaxis].T.astype(int)

# Normalisasi Min-Max pada data X
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Terapkan PCA pada data
pca = PCA(n_components=1)
X_transformed = pca.fit_transform(X_normalized)

# Bagi dataset menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Normalisasi Min-Max pada data X_train
scaler = MinMaxScaler()
X_train_normalized = scaler.fit_transform(X_train)

# Terapkan PCA pada data latih yang telah dinormalisasi
pca.fit(X_train_normalized)
X_train_transformed = pca.transform(X_train_normalized)

# Normalisasi Min-Max pada data X_test
X_test_normalized = scaler.transform(X_test)

# Terapkan PCA pada data uji yang telah dinormalisasi
X_test_transformed = pca.transform(X_test_normalized)

# Buat objek klasifikasi SVM
svm_classifier = SVC(kernel='rbf', random_state=42)

# Latih model menggunakan data latih
svm_classifier.fit(X_train_transformed, y_train)

# Lakukan prediksi menggunakan data uji
y_pred = svm_classifier.predict(X_test_transformed)

# Hitung akurasi model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Hitung precision, recall, dan F1-score
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# Hitung mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# # Membuat model
# from sklearn.externals import joblib

# # Simpan model ke file
# model_filename = "svm_model.pkl"
# joblib.dump(svm_classifier, model_filename)
# print("Model saved to", model_filename)

# # Muat model dari file
# loaded_model = joblib.load(model_filename)

# # Gunakan model yang telah dimuat untuk melakukan prediksi
# y_pred_loaded = loaded_model.predict(X_test_transformed)

# # Verifikasi apakah prediksi dari model yang dimuat sama dengan yang sebelumnya
# print("Are predictions equal?", np.array_equal(y_pred, y_pred_loaded))