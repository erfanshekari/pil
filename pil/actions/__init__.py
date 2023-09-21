from PIL import Image
from typing import List, Tuple, Any
from .square import square
from .resize import resize

def parser(actions: str) -> List[Tuple[str, Any]]:
    actions_ = []
    actions = actions.replace('"', '')
    for action in actions.split(';'):
        values = action.split(':')
        if len(values) == 2:
            actions_.append((values[0], values[1]))
        if len(values) == 1:
            if values[0]:
                actions_.append((values[0], None))
    return actions_

def handler(image: Image, actions: str) -> Image:
    print(parser(actions))
    for action in parser(actions):
        method, arg = action
        
        if method.lower() == 'square':
            image = square(image)

        if method.lower() == 'resize':
            image = resize(image, arg)
        
    return image