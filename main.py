import cv2
import numpy as np

#35698_ARHGAP25_Fbr_1_1
img = cv2.imread("35698_ARHGAP25_Fbr_1_1.tif", cv2.IMREAD_COLOR)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
