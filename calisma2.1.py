import cv2

resim = cv2.imread("cicek.jpg") #BGR - blue green red
cv2.imshow("Cicek Resmi", resim)

print(resim)
print(type(resim))
print(resim.size) #kaç tane piksel oldugunu gosteriyor
print(resim.dtype) #hangi datatypedan olustugunu gosteriyor
print(resim.shape) #resmin genislik yukseklik ve kac renk sklasindan olustugu
print(resim.item(100, 100, 0))

cv2.waitKey(0)
cv2.destroyAllWindows()