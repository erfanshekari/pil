# pil

pil is a cli tool that allows you to seamlessly convert and manipulate image formats.
pil cli uses python pillow which is highly fast and powerful.

## Features
* Format Conversion
     You can effortlessly convert images from one format to another. Simply specify the input and output formats, and the software will handle the conversion process.
* Image Optimization
    Pillow provides an effective image compression feature. It reduces the file size of images, optimizing them for storage and quicker transmission without compromising their visual quality.
* Image Compression
    The software provides efficient image compression capabilities. It reduces file sizes without compromising image quality, allowing for optimized storage and faster file transfer.
* Resizing Image
    You can easily resize images to fit specific dimensions or aspect ratios. The software ensures high-quality resizing with no loss of image details.
* Square Image
    By converting images into a square shape, the software ensures a uniform and visually appealing presentation. Square-cropped images are commonly used for social media profiles, galleries, and various applications where consistency in appearance is important.

## Installation
Make sure you have Python 3.8+, pip3 and venv installed before installing.
To install pil cli clone this repo and run install script:
~~~shell
git clone https://github.com/erfanshekari/pil.git
cd pil
sudo sh install.sh
~~~

## Usage
Use the --help flag for available items:
~~~shell
pil --help
~~~
~~~
usage: pil [...Options] -i INPUT -o OUTPUT

edit images on cmd, powerd by pillow and python

options:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        The input image can be a Unix path or url
  --actions ACTIONS, -a ACTIONS
                        Chain of actions
  --output OUTPUT, -o OUTPUT
                        The output path to save the image will be the current directory by default
  --overwrite           Overwrite an existing file
  --quality QUALITY, -q QUALITY
                        Spacify image quality
  --optimize, -O        Optimize image
~~~

Convert png to webp:
~~~shell
pil -i input_image.png -o output_image.webp
~~~

Compress image:
~~~shell
pil -q 90 -O -i input_image.png -o output_image.jpg
~~~

Resize image while maintaining aspect ratio:
~~~shell
pil -i input_image.png -a "resize:wx150;" -o output_image.jpg
~~~
~~~shell
pil -i input_image.png -a "resize:300xh;" -o output_image.jpg
~~~

Square image:
~~~shell
pil -i input_image.png -a "square;" -o output_image.jpg
~~~

Square and Resize image:
~~~shell
pil -i input_image.png -a "square;resize:150x150;" -o output_image.jpg
~~~

## License

This project is licensed under the [MIT License](LICENSE.md).