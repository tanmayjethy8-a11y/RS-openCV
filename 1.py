import cv2
import numpy as np

cap = cv2.VideoCapture(0)

canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# HSV range for blue color
lower_blue = np.array([100, 100, 100])
upper_blue = np.array([140, 255, 255])

prev_x, prev_y = 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Remove noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)

        if cv2.contourArea(c) > 100:
            x, y, w, h = cv2.boundingRect(c)

            cx = x + w // 2
            cy = y + h // 2

            cv2.circle(frame, (cx, cy), 8, (0, 0, 255), -1)

            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = cx, cy

            cv2.line(canvas,
                     (prev_x, prev_y),
                     (cx, cy),
                     (255, 255, 255),
                     5)

            prev_x, prev_y = cx, cy
    else:
        prev_x, prev_y = 0, 0

    output = cv2.add(frame, canvas)

    cv2.imshow("Virtual Drawing Board", output)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        canvas[:] = 0
        print("Canvas Cleared")

    elif key == ord('s'):
        cv2.imwrite("drawing.png", canvas)
        print("Drawing saved as drawing.png")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()