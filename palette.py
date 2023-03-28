import cv2
import matplotlib.pyplot as plt
import os.path
import pandas as pd
import color_module as clr_m

# ask user for file
filepath = input(f"Please provide the filepath of an image to analyze: ")
file_exists = os.path.exists(filepath)

if file_exists:
	
	# read user image into ndarray with cv2
	pic = cv2.imread(filepath)
	
	# create dataframe of rgb values using extract_rgb from color_module
	df_rgb = pd.DataFrame(clr_m.extract_rgb(pic))
	
	# create df_hex from df_rgb - adds hex values to df_rgb, 
	# converted from r,g,b columns using lambda and 
	# rgb2hex from color_module
	df_hex = df_rgb.assign(hex=df_rgb.astype(int).apply(
	lambda x: clr_m.rgb2hex(*x), axis=1))
	
	# create df_hex_byoccur, unique hex values listed from most often 
	# occurring in image to least
	df_hex_byoccur = df_hex.drop(['R', 'G', 'B'], axis=1).value_counts(ascending=False)
	
	# lists 10 colors from the image, excluding the first 5 to eliminate 
	# excess shades of a specific color
	print(df_hex_byoccur.iloc[5:15])

# if the image filepath provided didn't point to an image, end with msg	
else: 
	print("File not found.")
