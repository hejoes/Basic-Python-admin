import pandas as pd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature


pre_covid_flights = pd.read_csv('otselennud20.csv', delimiter=";")
after_covid_flights = pd.read_csv('otselennud23.csv', delimiter=";")

airports = pd.read_csv('https://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/airports.dat', delimiter=",")

airports = airports[['IATA', 'Latitude', 'Longitude', 'Altitude']]

pre_covid_flights_merged = pd.merge(pre_covid_flights, airports, on='IATA')
after_covid_flights_merged = pd.merge(after_covid_flights, airports, on='IATA')

# Salvestan info yhte faili, kuhu lisatud koordinaadid
pre_covid_flights_merged.to_csv('pre_covid_flights_merged.csv', index=False)

after_covid_flights_merged.to_csv('after_covid_flights_merged.csv', index=False)


# Loen andmeid mõlemast failist ja sean Tallinna punktist, kus hakatakse hiljem trajektoore joonestama
pre_covid_flights_readed = pd.read_csv('pre_covid_flights_merged.csv')
after_covid_flights_readed = pd.read_csv('after_covid_flights_merged.csv')
tallinn_data = pre_covid_flights_readed.iloc[1:]
tallinn_data2 = after_covid_flights_readed.iloc[1:]

# Mapi tegemine
proj = ccrs.PlateCarree()
fig, ax = plt.subplots(subplot_kw=dict(projection=proj))
ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=0.5)
ax.add_feature(cfeature.LAND)

#Joonestamise osa
for i, row in tallinn_data.iterrows():
    city = row['City']
    lat = row['Latitude']
    lon = row['Longitude']
    alt = row['Altitude']
    
    ax.plot([24.8328, lon], [59.4133, lat], transform=ccrs.Geodetic(), color="red", label=city, linewidth=1, alpha=0.7, zorder=1)
    ax.plot(lon, lat, marker='o', markersize=5, color='black', transform=proj, zorder=2)
    ax.text(lon, lat, city, transform=proj)

for i, row in tallinn_data2.iterrows():
    city = row['City']
    lat = row['Latitude']
    lon = row['Longitude']
    alt = row['Altitude']
    
    ax.plot([24.8328, lon], [59.4133, lat], transform=ccrs.Geodetic(), color="blue", label=city, linewidth=1, alpha=0.7, zorder=1)
    ax.plot(lon, lat, marker='o', markersize=5, color='black', transform=proj, zorder=2)
    ax.text(lon, lat, city, transform=proj)

ax.set_title('Otselennud Tallinnast. Henrik Jõesalu')

# LEGENDI TEGEMINE
red_handle = plt.Line2D([], [], color='red', linewidth=1, alpha=0.7, label='Pre-covid flights')
blue_handle = plt.Line2D([], [], color='blue', linewidth=1, alpha=0.7, label='After-covid flights')

# Loen kokku kui palju lende on igas otselennu failis
num_pre_covid_flights = len(pre_covid_flights_merged)
num_after_covid_flights = len(after_covid_flights_merged)

legend = ax.legend(handles=[red_handle, blue_handle], loc='lower left', fontsize=8, ncol=2)
legend.set_title('Lennud', prop={'size': 12})
legend._legend_box.align = "left"
legend.texts[0].set_text(f'Otselennud 2020, Kokku: {num_pre_covid_flights}')
legend.texts[1].set_text(f'Otselennud 2023, Kokku: {num_after_covid_flights}')

plt.show()
