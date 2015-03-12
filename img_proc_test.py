import cv2
import shutil
import numpy as np
shutil.copy2('base.tif', 'test.tif')

img = cv2.imread('test.tif', cv2.IMREAD_COLOR)

kernel = np.ones((5,5),np.uint8)
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img = cv2.GaussianBlur(img, (5,5), 0,0)

cv2.namedWindow('image1', flags = cv2.cv.CV_WINDOW_NORMAL)
cv2.namedWindow('image2', flags = cv2.cv.CV_WINDOW_NORMAL)

cv2.imshow("image1",img)
cv2.imshow("image2",img)
	
def erosion(r):
	x = cv2.getTrackbarPos('kernel','image1')
	kernel = np.ones((x,x),np.uint8)
	#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (x,x))
	global img_show1
	img_show1 = cv2.erode(img, kernel, iterations = cv2.getTrackbarPos('erosion','image1'))
	cv2.imshow("image1",img_show1-img_show2)
	
def dilation(r):
	x = cv2.getTrackbarPos('kernel','image2')
	kernel = np.ones((x,x),np.uint8)
	#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (x,x))
	global img_show2
	img_show2 = cv2.dilate(img, kernel, iterations = cv2.getTrackbarPos('dilation','image2'))
	cv2.imshow("image2",img_show2-img_show1)
	
# create trackbars for color change
cv2.createTrackbar('kernel','image1',1,64,erosion)
cv2.createTrackbar('erosion','image1',1,8,erosion)

# create trackbars for color change
cv2.createTrackbar('kernel','image2',1,64,dilation)
cv2.createTrackbar('dilation','image2',1,8,dilation)

#erosion(1)
#dilation(1)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.namedWindow('result', flags = cv2.cv.CV_WINDOW_NORMAL)
cv2.imshow("result",img_show1-img_show2)
cv2.waitKey(0)
cv2.imwrite('test.tif',img_show1-img_show2)
cv2.destroyAllWindows()