import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

ny_lon, ny_lat = -75, 43


plt.plot([ny_lon, ], [ny_lat, ],
         color='blue', linewidth=2, marker='o',
         transform=ccrs.Geodetic(),
         )

plt.plot([ny_lon], [ny_lat],
         color='gray', linestyle='--',
         transform=ccrs.PlateCarree(),
         )



plt.show()