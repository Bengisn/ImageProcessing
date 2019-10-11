import cv2
import numpy as np

resim = cv2.imread("resim.jpg")

#resim[50, 50] = [255, 255, 255] #resmin o pikseli beyaz olur
#print(resim[50,50]) #bir pikselin içinde bulunan bgr degerleri
#print("Resmin ozelligi = " + str(resim.shape)) #height width channel
#print("Resim boyutu = " + str(resim.size))
#print("Resim bit degeri = " + str(resim.dtype))

# for i in range(200):
#     resim[50, i] = [255, 255, 255] #cizgi halinde bir piksel serisini beyaz yaparız

# Bolge = resim[100:300, 200:400]
# resim[0:200, 0:200] = Bolge
# resim[0:200,200:400] = Bolge

#print(cv2.split(resim))
# b, g, r = cv2.split(resim)
# yeni_resim = cv2.merge((b,g,r))

#cv2.imshow("Kesilen bolge", Bolge)
#resim[:, :, 2] = 255 # 0=blue 1=green 2=red resfmin renk yogunlugunu degistiriyoruz

resim[100:200, 200:400, 2] = 255

cv2.imshow("Kedi Resmi Original", resim)
# cv2.imshow("Kedi Resmi Blue", r)
# cv2.imshow("Kedi Resmi Green", g)
# cv2.imshow("Kedi Resmi Red", b)
#cv2.imshow("Kedi Merge Edilmis Resim", yeni_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
