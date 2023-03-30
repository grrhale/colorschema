## Palette

Palette breaks down the colors that comprise a digital image and provides a visualization of the colors that appear in that image most often. Each pixel in a digital image is assigned a specific red, green, and blue value which, when combined, displays a particular color. These RGB values are more commonly represented in hexadecimal form, eg '#121212'. When you provide palette with an image, the program reads the RGB value of each pixel in that image. These values are converted to hexadecimal, and the ten most commonly occuring colors are graphed on a pi chart.   

A sample image file 'lily.jpg' is included in this github repository. When runningpalette, you will be prompted for a filepath. An example use case is as follows:

1) Open your terminal/CMD
2) Navigate to the directory palette.py and associated files are located in.
3) Type 'python3 palette.py'
4) You will be prompted to provide a filepath, ie: 'C:\Users\user\git\palette-main\lily.jpg
5) Wait a moment as the image is analyzed. A pie chart will be displayed that shows which hexadecimal colors appear most often, and in what ratio to each other.
 
# Requirements:

This program utilizes pandas for data manipulation, opencv to handle image data,
and matplotlib to generate a visualized output.

These libraries can be installed by running the following commands:

pip3 install pandas
pip3 install opencv-python
pip3 install matplotlib

#
