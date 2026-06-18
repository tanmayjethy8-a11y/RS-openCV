import cv2
import numpy as np
img = cv2.imread(r"C:\Users\HOME\OneDrive\Pictures\original_scenery image.jpeg")
img = cv2.resize(img, (500, 300))
b, g, r = cv2.split(img)
zero=np.zeros_like(b)
cv2.imshow("Blue Channel",cv2.merge([b,zero,zero]))
cv2.imshow("Green Channel",cv2.merge([zero,g,zero]))
cv2.imshow("Red Channel",cv2.merge([zero,zero,r]))

cv2.imwrite("Blue_Channel.png",cv2.merge([b,zero,zero]))
cv2.imwrite("Green_Channel.png",cv2.merge([zero,g,zero]))
cv2.imwrite("Red_Channel.png",cv2.merge([zero,zero,r]))
g = np.zeros_like(g)
merged = cv2.merge([b, g, r])

cv2.imshow("Merged Without Green", merged)
cv2.imwrite("Scenerywithoutgreen.jpg", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()