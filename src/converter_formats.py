from PIL import Image


def converter():
    im = Image.open('../assets/sad_cat.webp').convert("RGB")
    return im.save("../images/converted-image.png", "png")


if __name__ == '__main__':
    converter()
