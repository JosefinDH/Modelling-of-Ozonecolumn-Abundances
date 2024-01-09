#importering av bibliotek
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

#inläsning av datafil
fn = r"C:\Users\Josefin\Downloads\openmars_ozo_my27_ls2_my27_ls17.nc"
ds = nc.Dataset(fn)

#För att kunna se datafilens dimensioner och variabler -->
#for dim in ds.dimensions.values():
    #print(dim)
#for var in ds.variables.values():
    #print(var)

#Indexering av variabler ur datafilerna
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
#time = ds.variables['time'][:]
#Ls = ds.variables["Ls"][:]
#MY = ds.variables['MY'][:]

#val av intervall för longitud och latitud
latselect = np.logical_and(lats>-60, lats<60)
lonselect = np.logical_and(lons>-135,lons<135)

#Plottning av data
plt.figure(figsize=(8, 6))
contour = plt.contourf(lons, lats, ds.variables["o3col"][120,:,:], levels=35, cmap="nipy_spectral")
plt.colorbar(contour, label='µm-atm(mikrometer-atm)')

plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Total ozonkolumn för MY 27, Ls=2° – MY 27, Ls=17°')

#sparande och visande av plot
plt.savefig('GA(grafer)')
plt.show()