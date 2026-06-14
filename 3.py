import cv2
img = cv2.imread(r"c:\Users\HOME\OneDrive\Pictures\noise_remove.jpeg")
if img is None:
    print("Image not found!")
    exit()
noise_removed = cv2.medianBlur(img, 5)
cv2.imwrite("whithout_noise_image.png",noise_removed)
height, width, channels = img.shape
pixels = height * width

print("Height =", height)
print("Width =", width)
print("Channels =", channels)
print("Total Pixels =", pixels)

img_new=cv2.resize(img,(300,300))
clear_img=cv2.resize(noise_removed ,(300,300))

cv2.imshow("Original Image", img_new)
cv2.imshow("Clear Image", clear_img )

cv2.waitKey(0)
cv2.destroyAllWindows()