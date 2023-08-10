# spalette

spalette breaks down the colors that comprise a digital image and generates a color palette based on those colors. Each pixel in a digital image is assigned a specific red, green, and blue value which, when combined, displays a particular color. These RGB values are more commonly represented in hexadecimal form, eg '#121212'. Hex codes are regularly used in photo editing and graphic design contexts. When you provide palette with an image the program reads the RGB value of each pixel in that image. These values are quantized, and the quantized data is converted to hexadecimal. These colors are then ordered by occurrence and sampled to generate a color palette.

## How to run:

A sample image file 'lily.jpg' is included in this github repository. When running palette, you will be prompted for a filepath. You may provide a filepath to any image file on your machine (.jpg, .png, etc.) 

An example use case is as follows:

1) Open your terminal/CMD
2) Navigate to the directory palette.py and associated files are located in.
3) Type 'python3 palette.py'
4) You will be prompted to provide a filepath, ie: 'C:\Users\user\git\palette-main\lily.jpg. Simply type 'lily.jpg' if you run palette in the same folder you pull from here, as it is included as a sample image.
5) Wait a moment as the image is analyzed. A new window will open with a color palette in the form of a color wheel.
 
## Requirements:

This program utilizes pandas for data manipulation, opencv to read image data,
and matplotlib to generate a visual output. These need to be installed for the program to work.

These libraries can be installed by running the following commands:

* pip3 install pandas

* pip3 install opencv-python

* pip3 install matplotlib

These requirements are also listed in requirements.txt, which is prepared should you want to run this program in a virtual environment.

## Primary Features:

Reading Image Color Data
- Reads RGB values from digital image files into an array (ndarray).

Cleaning and Manipulating Image Color Data
- Creates a pandas dataframe of this data by extracting it from an ndarray and putting it into R, G, and B columns. Each row of this dataframe contains one pixel's color values. This dataframe is then converted to hexadecimal. The hexadecimal is added as an additional column, preserving the R G B values, and creating a master dataframe of all useful color data pixel by pixel. 

Sorting Image Data by Occurence
- This dataframe is then sorted into a pandas series, with the values that occur more often than others at the top and the values that occur least often at the bottom. This sort is then broken up into 10 equally sized sections for sampling. From these sections, the most often occuring color in each is selected and included in the palette. This is a primitive sampling method but it functions well for my purposes.
 
Visualizing the Occurence of Certain Colors
- These ten colors are then charted onto a pie chart, with each color being given equal space. The pie chart functions as a color wheel rather than a mathematical chart - this is our final color palette:

![alt text](https://i.imgur.com/hrVCxEi.png)
