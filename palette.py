import cv2
import matplotlib.pyplot as plt
import os.path
import pandas as pd
import color_module as clr_m

# ask user for file
filepath = input(f"Please provide the filepath of an image to analyze: ")
file_exists = os.path.exists(filepath)

if file_exists:
	"""
	reading data in
	"""
	# read user image into ndarray with cv2
	pic = cv2.imread(filepath)
	
	# create dataframe of the rgb values of every pixel in the image
	# using extract_rgb from color_module
	df_rgb = pd.DataFrame(clr_m.extract_rgb(pic))
	
	"""
	manipulating/cleaning the data
	"""
	# create dataframe df_hex from df_rgb - adds hex value column to 
	# df_rgb, converted from r,g,b columns using lambda and rgb2hex from 
	# color_module
	df_hex = df_rgb.assign(hex=df_rgb.astype(int).apply(
	lambda x: clr_m.rgb2hex(*x), axis=1))
	
	"""
	analyzing the data
	"""
	# create sr_hex_byoccur series: hexes are ordered from those 
	# occurring most often to least often in the image
	sr_hex_byoccur = df_hex.value_counts(ascending=False)
	
	"""
	visualizing the data
	"""
	# creates pie chart of the ten hexadecimal colors that appear the
	# most in the image file provided
	palette=sr_hex_byoccur.iloc[0:9]
	#p_colors = palette.to_dict()
	palette.plot.pie()
	plt.show()

# if the image filepath provided didn't point to an image, end with msg	
else: 
	print("File not found.")
