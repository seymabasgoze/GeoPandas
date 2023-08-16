import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# İstanbul'un shapefile veya GeoJSON dosyasının yolu
istanbul_gdf = gpd.read_file(r'C:\Users\stajyer\Downloads\istanbul-districts.json')

# CSV dosyasını aktarma
mekanlar = pd.read_csv(r'C:\Users\stajyer\Desktop\turist.csv', encoding='iso-8859-9')

# 'latitude' ve 'longitude' sütunlarını decimal türüne dönüştürme (dönüştürmeyince hata alınıyor)
mekanlar['latitude'] = mekanlar['latitude'].astype(float)
mekanlar['longitude'] = mekanlar['longitude'].astype(float)

# ziyaretçi sütununu int türüne dönüştürme (hata alınıyor yapmayınca)
mekanlar['ziyaretci'] = mekanlar['ziyaretci'].astype(int)

# GeoDataFrame'i oluşturma
gdf = gpd.GeoDataFrame(mekanlar, geometry=gpd.points_from_xy(mekanlar['longitude'], mekanlar['latitude']))
gdf = gdf.set_crs(epsg=4326)

# Harita figürünü oluşturma
fig, ax = plt.subplots(figsize=(10, 10))

# Harita sınırlarını belirleme
min_longitude = gdf['longitude'].min() - 0.1
max_longitude = gdf['longitude'].max() + 0.1
min_latitude = gdf['latitude'].min() - 0.1
max_latitude = gdf['latitude'].max() + 0.1
ax.set_xlim([min_longitude, max_longitude])
ax.set_ylim([min_latitude, max_latitude])

# İstanbul haritasını görselleştirme
istanbul_gdf.plot(ax=ax, color='lightblue', edgecolor='black')  # İstanbul haritasını çizdirin

# Mekanların yerini haritada gösterme-işaretleme
points = gdf.plot(ax=ax, marker='o', color='red', markersize=gdf['ziyaretci'] / 10000, label='Popüler Mekanlar')

# İlgili noktalara mekan adları ve ziyaretçi verilerini ekleme
annotations = []
for idx, row in gdf.iterrows():
    annotation = ax.annotate(f"{row['mekan_ad']} - {row['ziyaretci']}",
                             (row['geometry'].x, row['geometry'].y),
                             textcoords="offset points",
                             xytext=(0,10),
                             ha='center',
                             fontsize=8,
                             color='black',
                             visible=False)  # İlk başta verileri gösterme
    annotations.append(annotation)

# Mouse etkinliği işleme
def hover(event):
    if event.inaxes == ax:
        for point, annotation in zip(points.get_children(), annotations):
            contains, _ = point.contains(event)
            if contains:
                annotation.set_visible(True)
            else:
                annotation.set_visible(False)
        plt.draw()

fig.canvas.mpl_connect('motion_notify_event', hover)

# Diğer harita ayarlarını yapın
ax.set_title('İstanbul\'daki Popüler Turistik Mekanlar')
ax.set_xlabel('Boylam')
ax.set_ylabel('Enlem')
ax.legend()

plt.tight_layout()  # Grafik düzenini düzenler
plt.show()  # Haritayı görüntüleyin
