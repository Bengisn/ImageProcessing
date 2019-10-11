import cv2
import numpy as np #pyhonda daha az bellek kaplayan liste yapısı kutuphanelerini cagirmis oldum

resim = cv2.imread("supernatural.jpg") #flag=0 yaparsan resim siyah beyaz olacak, bos birakirsan renkli
#print(type(resim)) #resim degiskeni elimizide ne olarak tutuluyor
#cv2.imwrite("supernatural_gri.jpg", resim) #directory mizin içine kaydeder
resim2 = cv2.imread("supernatural_gri.jpg", 0)

cv2.imshow("Supernatural Image", resim) #resim = np array
cv2.imshow("Supernatural Image Gray", resim2)

cv2.waitKey(0) #herhangi bir tusa basmamizi bekler
cv2.destroyAllWindows() # x e basinca opencv'ye bagli tum pencereleri kapatir


