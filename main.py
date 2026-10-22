import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Baca dataset
df = pd.read_csv('dataset_mahasiswa.csv')

# Pisahkan fitur (X) dan label (y)
X = df[['IPK', 'SKS']]
y = df['Lulus']

# Split data (latih dan uji)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Uji beberapa nilai K
k_values = [1, 3, 5, 7, 9]
accuracies = []

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)
    print(f"K={k}, Akurasi={acc:.2f}")

# Tampilkan grafik perbandingan akurasi
plt.plot(k_values, accuracies, marker='o', color='blue')
plt.title('Perbandingan Akurasi Model KNN')
plt.xlabel('Nilai K (Jumlah Tetangga)')
plt.ylabel('Akurasi')
plt.grid(True)
plt.show()
