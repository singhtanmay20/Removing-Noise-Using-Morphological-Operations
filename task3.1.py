import cv2
import numpy as np

def trim(img,i,j):
	temp5=[[0 for u in range(len(structuring_element))] for v in range(len(structuring_element))]
	temp5=np.array(temp5)
	for x in range(0,len(structuring_element)):
		for y in range(0,len(structuring_element)):
			temp5[x,y]=img[i+x-(len(structuring_element)/2),j+y-(len(structuring_element)/2)]
	return temp5


def calculate_pixel_value(img):
	if np.array_equal(img, structuring_element)==True:
		return 255
	else:
		return 0

def calculate_pixel_value_dialation(img):
	match=0
	if np.array_equal(img, structuring_element)==True:
		return 255
	else:
		for i in range(5):
			for j in range(5):
				if structuring_element[i,j]==img[i,j]:
					match=match+1		
		if match==0:
			return 0
	return 255
		
def erosion(img):
	final_img=np.array([[0 for u in range(len(img[0]))] for v in range(len(img))])
	for i in range(len(structuring_element)/2,(len(img)-len(structuring_element)/2)):
		for j in range(len(structuring_element)/2,(len(img[0])-len(structuring_element)/2)):
			temp=trim(img,i,j)
			final_img[i,j]=calculate_pixel_value(temp)
	return final_img


def dilation(img):
	final_img=np.array([[0 for u in range(len(img[0]))] for v in range(len(img))])
	for i in range(len(structuring_element)/2,(len(img)-len(structuring_element)/2)):
		for j in range(len(structuring_element)/2,(len(img[0])-len(structuring_element)/2)):
			temp=trim(img,i,j)
			final_img[i,j]=calculate_pixel_value_dialation(temp)
	return final_img

def opening(img):
	erode=erosion(img)
	erode=erode/255
	dilate=dilation(erode)
	return dilate

def closing(img):
	dilate=dilation(img)
	dilate=dilate/255
	erode=erosion(dilate)
	return erode


def boundary_Extraction_Erosion(img):
	eroded_image=erosion(img/255)
	eroded_image=eroded_image.astype(np.uint8)
	boundary_erosion=res_noise1-eroded_image

	return boundary_erosion

def boundary_Extraction_Dilation(img):
	dilated_image=dilation(img/255)
	dilated_image=dilated_image.astype(np.uint8)
	boundary_dilation=dilated_image-res_noise1

	return boundary_dilation

img1=cv2.imread("/home/tanmay/Documents/cvip/proj_3/original_imgs/noise.png",0)
img1=np.array(img1)
structuring_element=np.ones((5,5))
img2=img1/255

res_noise1_1=opening(img2)
res_noise1=closing(res_noise1_1/255)

res_noise2_2=closing(img2)
res_noise2=opening(res_noise2_2/255)

res_bound1=boundary_Extraction_Erosion(res_noise1)
res_bound2=boundary_Extraction_Dilation(res_noise2)
cv2.imwrite('res_noise1.png',res_noise1)
cv2.imwrite('res_noise2.png',res_noise2)
cv2.imwrite('res_bound1.png',res_bound1)
cv2.imwrite('res_bound2.png',res_bound2)
cv2.waitKey(0)
cv2.destroyAllWindows()
