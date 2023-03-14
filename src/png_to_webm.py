from PIL import Image
from pathlib import Path


def converter(source):

    destination = source.with_suffix(".webp")
    im = Image.open(source)
    print('destination: ', destination)
    return im.save(destination, format="webp")


def main():
    paths = Path("webp").glob("**/*.png")
    for path in paths:
        webp_path = converter(path)
        print(webp_path)


main()
