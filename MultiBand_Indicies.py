from importlib.metadata import metadata
import rasterio
from rasterio.plot import show
from matplotlib import pyplot as plt


# Change the path to desired raster file
path = 'D:/Sem 3/Collab/Workspace/python/img1.tif'

img = rasterio.open(path) # raster file location, for easyiness just open the cmd in the raster image folder itself and poin the file name
print('Raster Image Information')
# open the image in a window
# show(img) 

read_img = img.read()
print('File Name:',img.name)
img_name = img.name
print('Profile:',img.profile)
# --------------------------------------------------------------------------------------------------------------------------
# Assining bands to variables for various indices

red_band = read_img[0].astype('f4')
nir_band = read_img[1].astype('f4')
import numpy as np

# as the some cell can have NAN, INF, or NINF as the value, numpy would give warning
# line below as it to ignore such cell values
np.seterr(invalid='ignore', divide='ignore') 
num= np.subtract(nir_band, red_band)
deno = np.add(nir_band, red_band)


# Code to calculate NDVI
ndvi_tmp = np.divide(num,deno)
ndvi = np.nan_to_num(ndvi_tmp,nan=-1)

plt.imshow(ndvi,cmap='viridis')
plt.colorbar()

# The naming follows file_name_NDVI
filename_tmp = img_name.rsplit(".",1)
filename = filename_tmp[0]
save_ndvi = filename + '_NDVI.PNG'
plt.savefig(save_ndvi)
print("NDVI plotting saved")

