from PIL import Image

import numpy as np

im = Image.open('sad_cat.webp').convert('RGBA')

data = np.array(im)
# just use the rgb values for comparison
rgb = data[:, :, :3]
color = [246, 213, 139]   # Original value
black = [0, 0, 0, 255]
white = [255, 255, 255, 255]
mask = np.all(rgb == color, axis= -1)
# change all pixels that match color to white
data[mask] = white

# change all pixels that don't match color to black
# data[np.logical_not(mask)] = black
new_im = Image.fromarray(data)
new_im.save("test_backgound.png", "png")
