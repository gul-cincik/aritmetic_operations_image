import cv2
import numpy as np

image1 = cv2.imread('messi.jpg')
image2 = cv2.imread('logo.jpg')

row, col, chanel = image2.shape
roi = image1[0:row, 0:col]

image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)#siyah beyaz yapan fonksiyon
ret, mask = cv2.threshold(image2_gray,10,255, cv2.THRESH_BINARY)#siyah beyaz tamamen
mas_inv = cv2.bitwise_not(mask)
cv2.imshow('mask', mask)
cv2.imshow('gray', image2_gray)
cv2.imshow('mask_inv', mas_inv),

image1_background = cv2.bitwise_and(roi, roi, mask=mas_inv)

image2_fg = cv2.bitwise_and(image2,image2, mask=mask)
cv2.imshow('mask_bacground', image1_background)
cv2.imshow('image2_fg', image2_fg)

image = cv2.add(image1_background, image2_fg)
image1[0:row, 0:col] = image

cv2.imshow('son_resim', image1)

cv2.waitKey(0)
cv2.destroyAllWindows()