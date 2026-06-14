import cv2
frame=cv2.imread("robot_vision.jpg")
gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cv2.rectangle(gray_frame,(10,10),(100,100),(0,255,0),3)
cv2.imshow("robotvision",gray_frame)
cv2.waitKey(1)