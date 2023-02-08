# lily.jpg was 720px * 540px originally

import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np
import os.path

# receive file from user
print("Please provide the filepath of an image to analyze:")
filepath = input()
file_exists = os.path.exists(filepath)

if file_exists:
	imageio.imread(filepath)
	
	pic=imageio.imread(filepath)

	print('Type of the image : ',type(pic))
	print('Shape of the image : {}'.format(pic.shape))
	print('Height of the image {}'.format(pic.shape[0]))
	print('Width of the image {}'.format(pic.shape[1]))
	print('Dimension of the image {}\n'.format(pic.ndim)) 

	print('Image size {}'.format(pic.size))
	print('Maximum RGB value in this image {}'.format(pic.max()))
	print('Minimum RGB value in this image {}\n'.format(pic.min())) 

	print('Value of only R channel {}'.format(pic[ 150, 100, 0]))
	print('Value of only G channel {}'.format(pic[ 150, 100, 1]))
	print('Value of only B channel {}'.format(pic[ 150, 100, 2])) 

	plt.title('R channel')
	plt.imshow(pic[ : , : , 0])
	plt.show()

	plt.title('G channel')
	plt.imshow(pic[ : , : , 1])
	plt.show() 

	plt.title('B channel')
	plt.imshow(pic[ : , : , 2])
	plt.show()

else: 
	print("File does not exist.")
