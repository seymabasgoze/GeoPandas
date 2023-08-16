import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import matplotlib.colors as mcolors
from matplotlib.colorbar import ColorbarBase

# Türkiye haritasını yükleme
turkey1 = gpd.read_file(r"C:\Users\stajyer\Downloads\data\TUR_adm0.shp")

# İklim verilerini bir CSV dosyasından okuma
data = pd.read_csv(r'C:\Users\stajyer\Downloads\Kitap1.csv', encoding='iso-8859-9')

# Grafik çizimi
plt.figure(figsize=(12, 6))
plt.plot(data['Yillar'], data['Sicaklik'], marker='o', label='Ortalama Sıcaklık')
plt.plot(data['Yillar'], data['Yagis'], marker='o', label='Ortalama Yağış')
plt.title('Yıllara Göre Ortalama Sıcaklık ve Yağış')
plt.xlabel('Yıl')
plt.ylabel('Değer')
plt.legend()
plt.grid()

# Renk paleti ve normalize işlemi
cmap = plt.get_cmap('Blues')  # Yağış için renk paleti
norm = mcolors.Normalize(vmin=data['Yagis'].min(), vmax=data['Yagis'].max())

# Her yıl için harita penceresi açma
for year in data['Yillar']:
    year_data = data[data['Yillar'] == year]

    # Yeni bir harita figürü oluştur
    plt.figure(figsize=(15, 10))

    # Türkiye haritasını çizdirme
    turkey1.boundary.plot(color='black', ax=plt.gca())

    # Haritayı renklendirme ve renk skalası oluşturma
    mappable = turkey1.plot(ax=plt.gca(), color=cmap(norm(year_data['Yagis'].values[0])), alpha=0.7)

    # Renk skalası oluşturma
    cax = plt.axes([0.85, 0.2, 0.03, 0.6])  # Renk skalası için yeni bir pencere oluştur
    cb = ColorbarBase(cax, cmap=cmap, norm=norm, label='Ortalama Yağış')

    plt.title(f'Türkiye İklim Verileri - {year} Yılı Yağış Renklendirmesi')
    plt.grid()
    plt.show()