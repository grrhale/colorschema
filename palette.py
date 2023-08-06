import cv2
import matplotlib.pyplot as plt
import os.path
import pandas as pd
import numpy as np
import color_module as clr_m

# ask user for file
filepath = input(f"Please provide the filepath of an image to analyze: ")
file_exists = os.path.exists(filepath)

if file_exists:
	"""
	Reading data in
	"""
	# Read user image into ndarray with cv2.
	pic = cv2.imread(filepath)
	
	# Create dataframe of the rgb values of every pixel in the image
	# using extract_rgb from color_module.
	df_rgb = pd.DataFrame(clr_m.extract_rgb(pic))
	
	"""
	Manipulating/cleaning the data
	"""
	# Create dataframe df_hex from df_rgb, adding hex value column to 
	# df_rgb. This is converted from r,g,b columns using a lambda and  
	# rgb2hex from color_module.
	df_hex = df_rgb.assign(hex=df_rgb.astype(int).apply(
	lambda x: clr_m.rgb2hex(*x), axis=1))

	"""
	Analyzing the data
	"""
	# Create srs_hex_byoccur series: hexes are ordered from those 
	# occurring most often to least often in the image. RGB values are
	# removed to make working with this series easier.
	srs_hex_byoccur = df_hex.drop(['R', 'G', 'B'], axis=1).value_counts(
	ascending=False)
	
	"""
	Visualizing the data
	"""
	# Create pie chart of a color palette
	
	df_10color_sample = np.array_split(srs_hex_byoccur, 10) # split the hex series into 10 equal parts
	df_sampled = pd.DataFrame({'hex': df_10color_sample[0].index[0]}) # define a dataframe to be populated with our palette
	for i in range(1, 10): # populate the dataframe
		df_sampled.loc[i] = df_10color_sample[i].index[0] # populating with first color in each equal part
		
	false_y=[5,5,5,5,5,5,5,5,5,5] # create false y axis to append to dataframe (to allow matplotlib to plot the palette as a pie chart)
	df_sampled['false_y']=false_y # append the false y data to the sampled dataframe
	
	df_sampled=df_sampled.set_index('hex') # set hex codes as index of the sampled dataframe

	
	colors=df_sampled.index.tolist() # Define colors, flattening df to list
	
	df_sampled.plot(kind='pie', y='false_y', colors=colors, legend=None) # plot the palette as an arbitrarily sized pie chart
	title_piechart='Palette from colors in ' + filepath # define the title for the palette chart
	plt.ylabel(None) # disable labeling of the ys, false data
	plt.title(label=title_piechart) # tell matplotlib to use our defined title
	plt.show() # plot the palette

# if the image filepath provided didn't point to an image, end with msg	
else: 
	print("File not found.")
