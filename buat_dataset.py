import pandas as pd
import random

# Buat dataset mahasiswa dengan 50 data
data = {
    'IPK': [round(random.uniform(2.5, 3.9), 2) for _ in range(50)],
    'SKS': [random.randint(100, 150) for _ in range(50)],
}

# Buat label "Lulus" berdasarkan logika sederhana
data['Lulus'] = [
    'Ya' if (ipk >= 3.2 and sks >= 125) else 'Tidak'
    for ipk, sks in zip(data['IPK'], data['SKS'])
]

# Simpan ke file CSV
df = pd.DataFrame(data)
df.to_csv('dataset_mahasiswa.csv', index=False)

print("✅ Dataset berhasil dibuat: dataset_mahasiswa.csv")
print(df.head())
