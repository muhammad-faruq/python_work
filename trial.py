import os
base_folder = 'C:/Users/faruq/Desktop/python_work'

import numpy as np

# ~ v = np.array([[1,2,3],[4,5,6],[7,8,9]])
# ~ a = np.array([1,2,3])
# ~ b = np.array([[1],[2],[3]])
# ~ print(a)
# ~ print(b)
# ~ print(a@b)
# ~ print(v[0])
# ~ print(v.shape)
# ~ print(v[1])
# ~ print(v[0,0])
# ~ v+=1
# ~ print(v)
from PIL import Image
# ~ from IPython.display import display

imgsFolder = os.path.join(base_folder,'src_images')
imageFilepath = os.path.join(imgsFolder,'image1.jpg')
img = Image.open(imageFilepath)
# ~ img.show()
W,H = img.size
print("Width = ", W)
print("Height = ", H)
img_array = np.array(img)
print("Shape of image = ", img_array.shape)

back2pil = Image.fromarray(img_array)
# ~ back2pil.show()
def stitch_lr(pil_img1,pil_img2):
	w1,h1 = pil_img1.size
	w1,h1 = w1//2, h1//2
	w2,h2 = pil_img2.size
	w2,h2 = w2//2, h1//2
	
	Hmax = max(h1,h2)
	pil_img1 = pil_img1.resize((w1,Hmax))
	pil_img2 = pil_img2.resize((w2,Hmax))
	
	img_arr1 = np.array(pil_img1)
	img_arr2 = np.array(pil_img2)
	stitched = np.hstack((img_arr1,img_arr2))
	return Image.fromarray(stitched)
	

img_lrflip = img.transpose(Image.FLIP_LEFT_RIGHT)
img_udflip = img.transpose(Image.FLIP_TOP_BOTTOM)
	
new_img = stitch_lr(img_udflip,img_lrflip)
new_img.show()

