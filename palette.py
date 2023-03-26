import cv2
import matplotlib.pyplot as plt
import numpy as np
import os.path
import pandas as pd
import color_module as cm

# ask user for file
filepath = input(f"Please provide the filepath of an image to analyze: ")
file_exists = os.path.exists(filepath)

if file_exists:
	# read user image into numpy ndarray with cv2
	pic = cv2.imread(filepath)	
	# create dataframe of rgb values
	df_rgb = pd.DataFrame(cm.extract_rgb(pic))
	# create df_hex from df_rgb, adding hex values and stripping RGB vals 
	df_hex = df_rgb.assign(
	hex=df_rgb.astype(int).apply(lambda r: cm.rgb2hex(*r), axis=1))
	
	# eliminate hex values that only appear once from the dataframe
	df_hex = df_hex[df_hex.duplicated(['hex'])]
	# eliminate the R G B values from the dataframe, leaving only recurring hexes
	df_hex = df_hex.drop(['R', 'G', 'B'], axis=1)
	# temporary print, to check results
	print(df_hex)

# if the image filepath provided didn't point to an image, end with msg	
else: 
	print("File not found.")
