from PIL import Image

def convert_png_to_jpg(image: Image) -> Image:
    return image.convert('RGB')

def convert_gif_to_jpg(image: Image) -> Image:
    return image.convert('RGB')

def handle_conversion(image: Image, from_ext: str, to_ext: str) -> Image:

    if from_ext == 'png' and to_ext == 'jpg' or to_ext == 'jpeg':
        return convert_png_to_jpg(image)
    
    if from_ext == 'gif' and to_ext == 'jpg' or to_ext == 'jpeg':
        return convert_gif_to_jpg(image)
    
    return image
