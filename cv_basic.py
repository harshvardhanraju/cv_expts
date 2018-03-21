import cv2
from matplotlib import pyplot as plt
Img_dir = "/home/harshavardhan/Desktop/poise.jpg"
img = cv2.imread(Img_dir)
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])
a = img2.item((2, 2, 2))
print(a)
img2.itemset((2, 2, 2), 0)
a = img2.item((2, 2, 2))
print(a)


plt.subplot(211)
plt.imshow(img)
plt.subplot(212)
plt.imshow(img2)
plt.show()

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
k = cv2.waitKey(0)

print(k)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    path = "/".join(Img_dir.split("/")[:-1])
    cv2.imwrite(path + "/test.jpg", img)
