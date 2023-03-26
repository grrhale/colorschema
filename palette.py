import cv2
import matplotlib.pyplot as plt
import numpy as np
import os.path
import pandas as pd
from itertools import product
import color_module as cm

# ask user for file
filepath = input(f"Please provide the filepath of an image to analyze: ")
file_exists = os.path.exists(filepath)

# declare rgb lists
r_vals=[]
g_vals=[]
b_vals=[]

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
	# combine lists into dictionary of rgb values
	rgb_data = {'R': r_vals, 'G': g_vals, 'B': b_vals}
	# create dataframe of rgb values
	df_rgb = pd.DataFrame(rgb_data)

	# convert rgb values to hexadecimal, and append them to the dataframe (as new df, df_hex) 
	df_hex = df_rgb.assign(
	hex=df_rgb.astype(int).apply(lambda r: cm.rgb2hex(*r), axis=1))
	# eliminate hex values that only appear once from the dataframe
	df_hex = df_hex[df_hex.duplicated(['hex'])]
	# eliminate the R G B values from the dataframe, leaving only recurring hexes
	df_hex = df_hex.drop(['R', 'G', 'B'], axis=1)
	# temporary prints, to check results
	df_hex.to_csv('lily.csv')
	print(df_hex)

# if the image filepath provided didn't point to an image, end with msg	
else: 
	print("File not found.")
