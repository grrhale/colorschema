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
filepath = input(f"Please provide the filepath of an image to analyze: ")
file_exists = os.path.exists(filepath)

#figure, plots = plt.subplots(ncols=3, nrows=1)

# declare rgb lists
r_vals=[]
g_vals=[]
b_vals=[]
# declare hexadecimal lists
hex_code = []
hex_list=[]
# declare i variable for loops
i = 0
	
if file_exists:
	
	# read user image into numpy ndarray with cv2
	pic = cv2.imread(filepath)
	# create list of coordinates of each pixel in the image
	coordinates = list(product(range(pic.shape[0]), range(pic.shape[1])))
	
	# loop to extract rgb values from each pixel by coordinate and add them to lists
	while i < len(coordinates):
		r_vals.append(format(pic[coordinates[i][0], coordinates[i][1], 2]))
		g_vals.append(format(pic[coordinates[i][0], coordinates[i][1], 1]))
		b_vals.append(format(pic[coordinates[i][0], coordinates[i][1], 0]))
		i += 1
	# combine lists into array of rgb values
	rgb_vals = np.array([r_vals, g_vals, b_vals])
	# create dataframe of values, rows = r,g,b, one column per pixel
	df_rgb = pd.DataFrame(rgb_vals)
	print('Analyzing...')
	
	for i in range(len(coordinates)):
		hex_code = [rgb2hex(
		int(df_rgb.iloc[0, i]), 
		int(df_rgb.iloc[1, i]), 
		int(df_rgb.iloc[2, i]))]
		hex_list.append(hex_code)

	df_hex = pd.DataFrame(hex_list)
	print(df_hex)
		

	
	
# if the image filepath provided doesn't point to an image, end with msg	
else: 
	print("File not found.")
