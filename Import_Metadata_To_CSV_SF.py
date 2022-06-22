import rasterio
import pandas as pd


# Chang file name and location in the variable below
input_data = 'D:/Sem 3/Collab/Workspace/Data/Sate_Image/tmp/LC09_L2SP_018028_20220121_20220124_02_T1/LIO.tif'

# Function to extract spatial resolution from a raster file
def resolution(raster):
    t = raster.transform
    x = t[0]
    y = t[4]
    return x,y

#  Function to extract SRID info from the raster file
# if AttributeError encountered then uncomment line 19 code and comment line 18 code
def crs(raster):
    return raster.crs.to_epsg()
    # return '4326'

# Function to extract no of bands in the raster file

def bands(raster):
    return raster.count

def read_metadata(raster):
    return raster.profile

def descp(raster):
    return raster.descriptions

def file_name(raster):
    return  raster.name.rsplit(".",1)[0]


def write_to_csv(filename,x_res,y_res,epsg,band,meta,desc,out_csv):
    d = {'file_name':[filename],'x_resolution':[x_res],'y_resolution':[y_res],'epsg':[epsg],'bands':[band],'meta':[meta],'description':[desc]}
    df = pd.DataFrame(data=d)
    df.to_csv(out_csv, mode='a', index=False, header=False)

if __name__=="__main__":
    raster = rasterio.open(input_data)
    out_csv = 'metadata.csv'
    name = file_name(raster)
    x_res, y_res = resolution(raster)
    epsg = crs(raster)
    band = bands(raster)
    meta = read_metadata(raster)
    desc = descp(raster)
    write_to_csv(name,x_res,y_res,epsg,band,meta,desc,out_csv)
print("Done")




