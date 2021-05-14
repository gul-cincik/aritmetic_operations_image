import cv2
import numpy as np

#toplama islemi
image1 = cv2.imread('resim.jpg')
image2 = cv2.imread('logo.jpg')

toplam = cv2.add(image1, image2)

cv2.imshow('toplam',toplam)

#ağırlıklı toplama
toplamA = cv2.addWeighted(image1, 0.7, image2, 0.3, 1)
cv2.imshow('agırlıklı toplam', toplamA)
cv2.waitKey(0)
cv2.destroyAllWindows()