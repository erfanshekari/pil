import os
from PIL import Image
from .file_size import file_size

def check_outpath_before_save(o: str) -> None:
    
    abs_path = os.path.abspath(o).split('/')

    current_dir = "/"
    for index, current in enumerate(abs_path):
        if index == (len(abs_path) - 1): break
        current_dir = os.path.join(current_dir, current)
        
        if not os.path.isdir(current_dir):
            os.mkdir(current_dir)

def print_image_info(image: Image, extension:str, size:int, label='INPUT') -> None:
    print(f'{label} {image.mode} ({extension}) {image.width}x{image.height} {file_size(size)}')

