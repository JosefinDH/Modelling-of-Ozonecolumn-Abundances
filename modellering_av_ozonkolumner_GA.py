import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

#Öppnade av datafilen
fn = r"openmars_ozo_my27_ls31_my27_ls45.nc"
ds = nc.Dataset(fn)

#För att kunna se datafilens dimensioner och variabler -->
#for dim in ds.dimensions.values():
    #print(dim)
#for var in ds.variables.values():
    #print(var)

#Indexering av variabler från datafilen
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
#time = ds.variables['time'][:]
#Ls = ds.variables["Ls"][:]
#MY = ds.variables['MY'][:]

#Val av intervall för longitud och latitud
latselect = np.logical_and(lats>-60, lats<60)

lonselect = np.logical_and(lons>-135,lons<135)

#Skapande av grafiska modeller
plt.figure(figsize=(8, 6))
contour = plt.contourf(lons, lats, ds.variables["o3col"][0,:,:], levels=30, cmap="nipy_spectral")
plt.colorbar(contour, label='µm-atm(mikrometer-atm)')

plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Total ozonkolumn för MY 27, Ls=2° – MY 27, Ls=17°')

#plt.grid(True, linestyle='--', alpha=0.6, color='black')
#plt.contour(lons[lonselect], lats[latselect], data, levels=10, colors='black', linewidths=0.5)
plt.savefig('GA_totalozonkolumn_graf_my27_ls2_my27_ls17')
plt.show()
