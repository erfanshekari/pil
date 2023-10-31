import io
import os
import requests
from posixpath import basename
from typing import Tuple
from urllib.parse import urlparse

from PIL import Image

from pil.exceptions import (
    OutPathAlreadyContainsFile,
    OutPathIsDirectory,
    FileNameWithNoExtension
)


def read_input_arg(i: str) -> bytes:
    if os.path.isfile(i):
        _ary = b''
        with open(i, 'rb') as f:
            _ary += f.read()
        return _ary
    else:
        _ary = b''
        with requests.get(i, stream=True, timeout=5) as r:
            r.raise_for_status()
            for chunk in r.iter_content(5 * 1024):
                _ary += chunk
        return _ary


def bytes_to_image(b: bytes) -> Image:
    return Image.open(io.BytesIO(b))


def read_output_arg(o: str) -> None:
    if os.path.isfile(o):
        raise OutPathAlreadyContainsFile(
            "The output path you specified already contains a file. If you want to overwrite an existing file, you must add the --overwrite flag.")

    if os.path.isdir(o):
        raise OutPathIsDirectory("Output path is directory!")


def export_filename_extension_from_unix_path(path: str) -> Tuple[str, str]:
    filename = '.'.join(basename(path).split('.')[:-1])
    extension = basename(path).split('.')[-1]
    return filename, extension


def parse_input_filename(i: str) -> Tuple[str, str]:
    as_url = urlparse(i)
    if as_url.hostname:
        return export_filename_extension_from_unix_path(as_url.path)
    if '.' not in i:
        raise FileNameWithNoExtension(
            "The input filename does not have an extension, so you must specify a filename with the extension in the output.")
    return export_filename_extension_from_unix_path(i)
