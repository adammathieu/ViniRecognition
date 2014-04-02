import numpy as np
import cv2

img = cv2.imread('../Images/domtaillandier_appsavennieresctrl_2009_000002.jpg')

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()