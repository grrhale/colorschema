import cv2
import matplotlib.pyplot as plt
import numpy as np
import os.path
import pandas as pd

# ask user for file
print("Please provide the filepath of an image to analyze:")
filepath = input()
file_exists = os.path.exists(filepath)

"""
 read file given by user if it exists,
 then print information about the image. after, plot the R G B channels.
"""
#figure, plots = plt.subplots(ncols=3, nrows=1)

if file_exists:
	# read user image into numpy ndarray
	pic = cv2.imread(filepath)
	# convert image to grayscale for np.where
	gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
	# create array of xy coordinates of each pixel in the image using np.where
	xy_coords = np.flip(np.column_stack(np.where(gray >= 0)), axis=1)
	
	for i in xy_coords:
		x=(i[0])
		y=(i[1])
		red_values = format(pic[x, y, 2])
		green_values = format(pic[x, y, 1])
		blue_values = format(pic[x, y, 0])
		
		pixel_values = (red_values, green_values, blue_values)
		print(pixel_values)
# print information about the file
#	print('Type of the image: ',type(pic))
#	print('Shape of the image: {}'.format(pic.shape))
#	print('Height of the image: {}'.format(pic.shape[0]))
#	print('Width of the image: {}'.format(pic.shape[1]))
#	print('Dimension of the image: {}\n'.format(pic.ndim)) 

#	print('Image size {}'.format(pic.size))
#	print('Maximum RGB value in this image {}'.format(pic.max()))
#	print('Minimum RGB value in this image {}\n'.format(pic.min())) 

#	print('Value of only R channel {}'.format(pic[100, 150, 2]))
#	print('Value of only G channel {}'.format(pic[100, 150, 1]))
#	print('Value of only B channel {}'.format(pic[100, 150, 0])) 

# plot the red green and blue channels
#	for i, subplot in zip(range(3), plots):
#		temp = np.zeros(pic.shape, dtype='uint8')
#		temp[:,:,i] = pic[:,:,i]
#		subplot.imshow(temp)
#		subplot.set_axis_off()
#	plt.show()

# if the image filepath provided doesn't point to an image, end with msg	
else: 
	print("File not found.")
