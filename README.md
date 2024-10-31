# MifImgConverter
## Description
This program will take a Intel Memory Initialization File (.mif) containing the initiazation data necessary to display images through VGA on an FPGA board. The programs in this project were created for use in the ECE241 Course at the University of Toronto

imagetomif.py will take in an image and ouput a .mif file
miftoimage.py will take in a .mif and output an image file

To use the MifImgConverter, either clone this repository with
>git clone (https://github.com/RoZ4/MifImgConverter.git)
or copy the python script directly to your machine

You will require the Python Imaging Library (Pillow) to be installed before using either conversion program

## How to Use
In a command shell, run
>	python miftoimage.py -h
or
>	python imagetomif.py -h
to view the corrosponding commands for each conversion tool

You will need to specify:
1. An input file location
2. An output file location
3. (imagetomif.py ONLY) the number of hexidecimal values to allocate each R,G, and B channel of each pixel (default 1, meaning the mif stores colours in 3 hexicimal values, or 12 bits)

