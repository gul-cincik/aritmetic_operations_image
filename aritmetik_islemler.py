import cv2
image = cv2.imread('saat.jpg')


print(image[80,80])#80e 80 pikselinde hangi rengin olduğunu rgb cinsinden verir
image[80,80] = [255, 255, 255]
bolge = image[30:120, 100:200]
image[30:120, 100:200] = [255, 255, 255]
image[0:90,0:100] = bolge
cv2.rectangle(image,(100,30), (200,120), (0,255,0), 2)
cv2.imshow('Saat', image)
cv2.imshow('bolge', bolge)
cv2.waitKey(0)
cv2.destroyAllWindows()
