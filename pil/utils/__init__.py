import os


def check_outpath_before_save(o: str) -> None:
    
    abs_path = os.path.abspath(o).split('/')

    current_dir = "/"
    for index, current in enumerate(abs_path):
        if index == (len(abs_path) - 1): break
        current_dir = os.path.join(current_dir, current)
        
        if not os.path.isdir(current_dir):
            os.mkdir(current_dir)