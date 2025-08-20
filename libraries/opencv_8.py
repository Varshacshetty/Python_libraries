import cv2
import numpy as np
# Create an image (black background)
img = np.zeros((200, 200, 3), dtype="uint8")

# Draw a red circle
cv2.circle(img, (100, 100), 50, (0, 0, 255), -1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
