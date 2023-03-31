# Palette

Palette breaks down the colors that comprise a digital image and provides a visualization of the colors that appear in that image most often. Each pixel in a digital image is assigned a specific red, green, and blue value which, when combined, displays a particular color. These RGB values are more commonly represented in hexadecimal form, eg '#121212'. Hex codes are regularly used in photo editing software such as Photoshop. When you provide palette with an image the program reads the RGB value of each pixel in that image. These values are converted to hexadecimal, and the ten most commonly occuring colors are graphed in a pie chart.

A sample image file 'lily.jpg' is included in this github repository. When runnin palette, you will be prompted for a filepath. You may provide a filepath to any image file on your machine (.jpg, .png, etc.) 

An example use case is as follows:

1) Open your terminal/CMD
2) Navigate to the directory palette.py and associated files are located in.
3) Type 'python3 palette.py'
4) You will be prompted to provide a filepath, ie: 'C:\Users\user\git\palette-main\lily.jpg. Simply type 'lily.jpg' if you run palette in the same folder you pull from here, as it is included as a sample image. It contains a surprising amount of white and shades of white.
5) Wait a moment as the image is analyzed. A pie chart will be displayed that shows which hexadecimal colors appear most often, in relation to each other.
 
## Requirements:

This program utilizes pandas for data manipulation, opencv to read image data,
and matplotlib to generate a visualized output. These need to be installed for the program to work.

These libraries can be installed by running the following commands:

* pip3 install pandas

* pip3 install opencv-python

* pip3 install matplotlib

## Primary Features:

Reading Image Color Data
- Reads RGB values from digital image files into an array (ndarray).

Cleaning and Manipulating Image Color Data
- Creates a pandas dataframe of this data by extracting it from an ndarray and putting it into R, G, and B columns. Each row of this dataframe contains one pixel's color values. This dataframe is then converted to hexadecimal. The hexadecimal is added as an additional column, preserving the R G B values, and creating a master dataframe of all useful color data pixel by pixel. 

Sorting Image Data by Occurence
- This dataframe is then sorted into a pandas series, with the values that occur more often than others at the top and the values that occur least often at the bottom. This sort is further narrowed to the ten most often occuring hex values.

Visualizing the Occurence of Certain Colors
- The ten most often occuring hex values are then plotted to a pie chart, and displayed to the user. 

Often one color, such as #ffffff (white), will dominate an image. Other shades of this color may also occur disproportionately to those that make up the image's subject. It can be useful to know if certain hex value should be filtered out of an image, or another made to stand out in relation to it, when manipulating an image with other software.      

![alt text](https://imgur.com/yb5s7SK)

### CODE LOUISVILLE NOTE

In my project plan, I set out to create a program that generates a color palette from the colors present in an image. Palette visualizes the colors which are most common in an image, but this does not result in a true color palette. This data is still useful however in certain photo editing scenarios.

