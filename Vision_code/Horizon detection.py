import cv2
import numpy as np
def nothing(x):
    pass

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L – H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L – S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L – V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U – H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U – S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U – V", "Trackbars", 255, 255, nothing)

# img =cv2.imread("bitbots-montreal-test01_003263.jpg")
# img =cv2.imread("bitbots-montreal-test01_000000.jpg")
img =cv2.imread("football_grnd.png")
# img =cv2.imread("bitbots-montreal-test01_0032226.jpg")

img=cv2.GaussianBlur(img,(5,5),3)
canny=np.zeros(np.shape(img))
canny=cv2.Canny(img,100,150)
cv2.imshow("Img1",img)
while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L – H", "Trackbars")
    l_s = cv2.getTrackbarPos("L – S", "Trackbars")
    l_v = cv2.getTrackbarPos("L – V", "Trackbars")
    u_h = cv2.getTrackbarPos("U – H", "Trackbars")
    u_s = cv2.getTrackbarPos("U – S", "Trackbars")
    u_v = cv2.getTrackbarPos("U – V", "Trackbars")
    # lower_value = np.array([31, 100, 0])
    # upper_value = np.array([120, 255, 180])
    lower_value = np.array([l_h, l_s, l_v])
    upper_value = np.array([u_h, u_s, u_v])

    mask= cv2.inRange(hsv,lower_value,upper_value)
    canny = cv2.Canny(mask, 100, 100)
    cv2.imshow("canny",canny)

    key=cv2.waitKey(1)
    if key==27:
        break



lines = cv2.HoughLinesP(canny, 1, np.pi / 180,1)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
cv2.imshow("Image Line",img)

result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()