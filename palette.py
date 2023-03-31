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
	# Create pie chart of the ten hexadecimal colors that appear the
	# most in the image file provided.
	palette=srs_hex_byoccur.iloc[0:9] # Grab a series of ten most often occuring colors with iloc
	
	p_c=list(palette.to_dict().keys()) # Convert series to dictionary, but keys only (leaving only hex values)
	colors=[x[:1] for x in p_c] # Define colors, flattening dict to list
	colors=[list(x) for x in colors] # Collapse list from list of lists that contain single hex values, to list of hex values
	final_plot_colors=[x for colors in colors for x in colors] 
	
		
	palette.plot.pie(colors=final_plot_colors) # Plot pie chart of colors
	title_piechart='Hexadecimal colors which occur most often in ' + filepath
	plt.ylabel(None)
	plt.title(label=title_piechart)
	plt.show()

# if the image filepath provided didn't point to an image, end with msg	
else: 
	print("File not found.")
