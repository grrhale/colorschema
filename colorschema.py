# lily.jpg was 720px * 540px originally

#import imageio
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import cv2
from skimage.color import rgb2lab, deltaE_cie76
from collections import Counter
import os

pic=imageio.imread('/home/rhale/git/colorschema/lily.jpg')

print('Type of the image : ',type(pic))
print('Shape of the image : {}'.format(pic.shape))
print('Height of the image {}'.format(pic.shape[0]))
print('Width of the image {}'.format(pic.shape[1]))
print('Dimension of the Image {}\n'.format(pic.ndim)) 

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
