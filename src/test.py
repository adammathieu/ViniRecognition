import numpy as np
import cv2

try:
	img = cv2.imread('../Images/domtaillandier_appsavennieresctrl_2009_000002.jpg',cv2.CV_LOAD_IMAGE_GRAYSCALE)
except IOError:
	print "unable to read files"

h,w = img.shape
print h,w

img_resize = cv2.resize(img,(0,0),fx=0.3, fy=0.3)
h,w = img_resize.shape
print h,w

cv2.imshow('image',img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()