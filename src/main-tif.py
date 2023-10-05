from PIL import Image

image = "../assets/tifs/STScI-01FYSBA8TGP7M3MWKQTV75N7DQ.tif"
# Load the TIFF image file
with Image.open(image) as img:
    # Display image properties
    print(f"Format: {img.format}")
    print(f"Mode: {img.mode}")
    print(f"Size: {img.size}")
    print(f"Info: {img.info}")

    # If you want to see more details such as metadata
    metadata = img.tag_v2
    print(f"Metadata: {metadata}")


import rioxarray

# Load the TIFF image file into an xarray DataArray
data_array = rioxarray.open_rasterio(image)

# Display the dimensions and coordinates which includes channels
print(data_array.dims)
print(data_array.coords)

# If the TIFF file has multiple layers, they will be represented as bands in the DataArray
print(f'Number of layers (bands): {data_array.sizes["band"]}')

# To access a specific layer (band), you can use indexing
# For example, to access the first layer:
first_layer = data_array.sel(band=1)
print(first_layer)
