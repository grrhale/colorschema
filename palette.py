import cv2
import matplotlib.pyplot as plt
import numpy as np
import os.path

# ask user for file
print("Please provide the filepath of an image to analyze:")
filepath = input()
file_exists = os.path.exists(filepath)

"""
 read file given by user if it exists,
 then print information about the image. after, plot the R G B channels.
"""
figure, plots = plt.subplots(ncols=3, nrows=1)
pic = cv2.imread(filepath)

if file_exists:
	cv2.imread(filepath)

# print information about the file
	print('Type of the image: ',type(pic))
	print('Shape of the image: {}'.format(pic.shape))
	print('Height of the image: {}'.format(pic.shape[0]))
	print('Width of the image: {}'.format(pic.shape[1]))
	print('Dimension of the image: {}\n'.format(pic.ndim)) 

	print('Image size {}'.format(pic.size))
	print('Maximum RGB value in this image {}'.format(pic.max()))
	print('Minimum RGB value in this image {}\n'.format(pic.min())) 

	print('Value of only R channel {}'.format(pic[100, 150, 2]))
	print('Value of only G channel {}'.format(pic[100, 150, 1]))
	print('Value of only B channel {}'.format(pic[100, 150, 0])) 

# plot the red green and blue channels
	for i, subplot in zip(range(3), plots):
		temp = np.zeros(pic.shape, dtype='uint8')
		temp[:,:,i] = pic[:,:,i]
		subplot.imshow(temp)
		subplot.set_axis_off()
	plt.show()

# if the image filepath provided doesn't point to an image, end with msg	
else: 
	print("File not found.")
