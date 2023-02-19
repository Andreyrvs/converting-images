from PIL import Image

im = Image.open('./assets/sad_cat.webp').convert("RGB")
im.save("./images/converted-image.png", "png")
