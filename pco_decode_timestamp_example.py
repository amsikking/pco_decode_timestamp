from tifffile import imread
from pco_decode_timestamp import decode_timestamp

# example -> how to get timestamps from an image stack:
images = imread('pco_timestamp_example.tif')
print(images.shape)

for image in range(images.shape[0]):
    timestamp = decode_timestamp(images[image,:,:])
    print('image: %03i (%ius)'%(timestamp['#'], timestamp['us']))
