import fiona
import rasterio
import rasterio.mask

# Change the two variables below to the concerened directory.
shp_path = 'D:/Sem 3/Collab/shp_tmp.shp'
path1 = 'LIO.tif'

with fiona.open(shp_path,'r') as shapefile:
    for feature in shapefile:
        shapes = [feature['geometry']]
        print(shapes) 

with rasterio.open(path1) as src:
    out_img, out_transform = rasterio.mask.mask(src, shapes, crop=True)
    out_meta = src.meta
    out_meta.update({'driver': 'GTiff',
                 'height': out_img.shape[1],
                 'width': out_img.shape[2],
                 'transform': out_transform})

with rasterio.open('mask1.tif','w',**out_meta) as dest:
    dest.write(out_img)

print("Done")
