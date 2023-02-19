from PIL import Image

im = Image.open('sad_cat.webp').convert("RGB")
im.save("converted-image.png", "png")
