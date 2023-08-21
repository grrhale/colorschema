# spalette - a simple command line color palette tool

spalette analyzes the colors that comprise a digital image and generates a color palette from them. When you provide spalette with an image the program quantizes it, simplifying the number of colors available while maintaining true to the original colors. Each pixel of the quantized image is read in RGB format, then converted to hexadecimal format. These hex color codes are then ordered by occurrence and sampled (the ordered list is split into ten equal parts, and the most often occuring color in each part becomes one element of the color palette). This process results in a ten color palette drawn from the full range of colors present in the image.

## Requirements & Installation:

spalette version 0.1 is currently available for installation through the Python Package Index. You may install the program from the command line using the "pip" command line tool as follows: `pip install spalette`

Using pip, the necessary python dependencies should be installed for you.

If you would prefer to install spalette from source, there are a few dependencies you will need to install prior to installation. spalette utilizes Pandas and NumPy for data manipulation, OpenCV to read image data,
and Matplotlib to generate a visual output. These need to be installed for the program to work, and you can do that with the following command:

`pip install pandas numpy opencv-python matplotlib`

## Usage:

On Mac and Linux, spalette should automatically be added to your $PATH and be ready to run as a command after installing with pip. On Windows, you may have to add Python programs to your $PATH manually for it to be available. You can find the steps to do that [here.](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) This will no longer be an issue in the next release.

spalette is meant to be as simple as possible, requiring only one input: the filepath to an image. In a terminal or command prompt, type:
 `spalette path/to/imagefile.jpg`  

A color palette will be generated and the default output of ten hex color codes will appear on the CLI. This is your color palette, ready to be used as you see fit. For a visual representation of the palette in addition to the list, include `-cw` before or after the filepath like so:
`spalette -cw path/to/imagefile.jpg`

 A new window will open with the ten palette colors plotted onto a color wheel. You may save this wheel as a reference, or simply close it if you are done. 

## Detailed feature list and technical information:

#### Reads image color data:
- Reads RGB values from provided image files into an array (ndarray - numpy dependency).

#### Cleans and manipulates this color data to create an output:
- The image file is quantized to simplify the color data available while staying true to the colors present in the image. The program creates a pandas dataframe of this data by extracting it from the ndarray and putting it into R, G, and B columns. Each row of this dataframe contains one pixel's color values. This dataframe is then converted to hexadecimal which is added as an additional column, preserving the R G B values and creating a master dataframe of all useful color data pixel by pixel. 

- This dataframe is then sorted into a pandas series, with the values that occur more often than others at the top and the values that occur least often at the bottom. This sort is then broken up into 10 equally sized sections (using NumPy's array_split function) for sampling. From these sections, the most often occurring color in each is selected and included in the palette.
 
#### Visualizes the generated color palette:
- These ten colors are always output to the terminal for you to use as you see fit. They may also be visualized as a color wheel (matplotlib pie chart with each color being given equal space) if so desired by passing '-cw' when running:

![alt text](https://i.imgur.com/hrVCxEi.png)
## Features planned for version 0.2:
- the ability for the user to choose how many colors comprise the palette
- multiple quantization options, allowing for better palette generation from overly light or dark images
- the ability to automatically output the palette to a file without interacting with the matplotlib GUI
- a secondary visualization option
