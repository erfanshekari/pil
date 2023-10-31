from math import log2

_suffixes = ['bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']


def file_size(size: int) -> str:
    order = int(log2(size) / 10) if size else 0

    return '{:.4g} {}'.format(size / (1 << (order * 10)), _suffixes[order])
