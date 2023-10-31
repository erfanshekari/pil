from PIL import Image


def square(image: Image) -> Image:
    if image.width == image.height:
        return image

    left, top, right, bottom = 0, 0, 0, 0

    if min(image.width, image.height) == image.width:

        right = image.width
        top = (image.height - image.width) / 2
        bottom = ((image.height - image.width) / 2) + image.width

    else:

        left = (image.width - image.height) / 2
        right = ((image.width - image.height) / 2) + image.height
        bottom = image.height

    return image.crop((left, top, right, bottom))
