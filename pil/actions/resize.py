from PIL import Image

def resize(image: Image, arg: str) -> Image:
    
    width, height = arg.split('x')

    is_var = lambda x: True if x == 'w' or x == 'h' else False

    if is_var(width):
        ratio = image.width / image.height
        width = int(float(height) * ratio)

    if is_var(height):
        ratio = image.height / image.width
        height = int(float(width) * ratio)

    return image.resize((int(width), int(height)))

