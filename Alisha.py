import pandas as pd
import matplotlib.pyplot as plt

# Membaca file data
data = pd.read_csv('Alisha.csv')

# Menampilkan lima baris pertama data
print("Lima baris pertama data:")
print(data.head())

# Menampilkan informasi umum tentang data
print("\nInformasi umum tentang data:")
print(data.info())

# Menampilkan ringkasan statistik tentang data numerik
print("\nRingkasan statistik tentang data:")
print(data.describe())

# Menampilkan jumlah data yang hilang (missing values) dalam setiap kolom
print("\nJumlah data yang hilang dalam setiap kolom:")
print(data.isnull().sum())

# Menampilkan jumlah unik dari setiap nilai dalam suatu kolom
print("\nJumlah nilai unik dalam setiap kolom:")
print(data.nunique())

# Menampilkan tipe data dari setiap kolom
print("\nTipe data dari setiap kolom:")
print(data.dtypes)

# Scatter Plot
plt.subplot(2, 2, 1)
plt.scatter(data['umur'], data['pendapatan'], color='blue', alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('Umur')
plt.ylabel('Pendapatan')

# Histogram
plt.subplot(2, 2, 2)
plt.hist(data['pendapatan'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Pendapatan')
plt.xlabel('Pendapatan')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(2, 2, 3)
plt.boxplot(data['umur'].dropna())
plt.title('Box Plot of Umur')
plt.ylabel('Umur')

# Membuat data untuk barplot jenis kelamin
gender_data = data['jenis_kelamin'].value_counts().index.tolist()
count_data = data['jenis_kelamin'].value_counts().tolist()

# Membuat barplot
plt.subplot(2, 2, 4)
plt.bar(gender_data, count_data, color=['blue', 'pink'])
plt.title('Barplot Jenis Kelamin')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Jumlah')

# Menampilkan semua visualisasi dalam satu window
plt.tight_layout()
plt.show()
