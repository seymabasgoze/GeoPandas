import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

# Türkiye haritasını yükleme
turkey1 = gpd.read_file(r"C:\Users\stajyer\Downloads\data\TUR_adm0.shp")

# İklim verilerini bir CSV dosyasından okuma
data = pd.read_csv(r'C:\Users\stajyer\Downloads\Kitap1.csv', encoding='iso-8859-9')

# Çizgi grafiğini oluşturma
plt.figure(figsize=(10, 6))

# Tüm yılları içeren sıcaklık verilerini çizdirme ve renklendirme
plt.scatter(data['Yillar'], data['Sicaklik'], c=data['Sicaklik'], cmap='coolwarm', marker='o', label='Ortalama Sıcaklık')
plt.colorbar(label='Ortalama Sıcaklık')

# Tüm yılları içeren yağış verilerini çizdirme
plt.plot(data['Yillar'], data['Yagis'], marker='o', label='Ortalama Yağış')

# Haritayı çizdirme
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
turkey1.boundary.plot(ax=ax, color='black')  # Sadece sınırları çizdirme

plt.title('Türkiye İklim Verileri - (2000-2021)')
plt.xlabel('Yıl')
plt.ylabel('Değer')
plt.legend()
plt.grid()
plt.show()