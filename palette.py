import cv2
import matplotlib.pyplot as plt
import numpy as np
import os.path
import pandas as pd
from itertools import product

# function to convert rgb values to hexadecimal values
def rgb2hex(red, green, blue):
	return '#%02x%02x%02x' % (red, green, blue)

# ask user for file
print("Please provide the filepath of an image to analyze:")
filepath = input()
file_exists = os.path.exists(filepath)

"""
 read file given by user if it exists,
 then print information about the image. after, plot the R G B channels.
"""
#figure, plots = plt.subplots(ncols=3, nrows=1)
i = 0

if file_exists:
	
	# read user image into numpy ndarray with cv2
	pic = cv2.imread(filepath)
	# create list of coordinates of each pixel in the image
	coordinates = list(product(range(pic.shape[0]), range(pic.shape[1])))
	
	# declare rgb lists
	rl=[]
	gl=[]
	bl=[]
	
	# loop to extract rgb values from each pixel and add them to lists
	while i < len(coordinates):
		rl.append(format(pic[coordinates[i][0], coordinates[i][1], 2]))
		gl.append(format(pic[coordinates[i][0], coordinates[i][1], 1]))
		bl.append(format(pic[coordinates[i][0], coordinates[i][1], 0]))
		i += 1
	# combine lists into array of rgb values
	rgb_vals = np.array([rl, gl, bl])
	# create dataframe of values, rows = r,g,b, one column per pixel
	df_rgb = pd.DataFrame(rgb_vals)
	
	for i in range(pic.size):
		print(rgb2hex(int(df_rgb.iloc[0, i]), int(df_rgb.iloc[1, i]), int(df_rgb.iloc[2, i])))

	
	
# if the image filepath provided doesn't point to an image, end with msg	
else: 
	print("File not found.")
