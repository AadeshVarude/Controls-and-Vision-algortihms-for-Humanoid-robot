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

img =cv2.imread("bitbots-montreal-test01_003263.jpg")
# img =cv2.imread("bitbots-montreal-test01_000000.jpg")
# img =cv2.imread("football_grnd.png")
# img =cv2.imread("test_lab.jpg")
a=np.shape(img)
x=a[0]
y=a[1]
img=cv2.GaussianBlur(img,(3,3),10)
canny=np.zeros(np.shape(img))
canny=cv2.Canny(img,100,150)
# cv2.imshow("Img1",img)
while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L – H", "Trackbars")
    l_s = cv2.getTrackbarPos("L – S", "Trackbars")
    l_v = cv2.getTrackbarPos("L – V", "Trackbars")
    u_h = cv2.getTrackbarPos("U – H", "Trackbars")
    u_s = cv2.getTrackbarPos("U – S", "Trackbars")
    u_v = cv2.getTrackbarPos("U – V", "Trackbars")
    # lower_value = np.array([121, 100, 31.4])
    # upper_value = np.array([170, 100, 31.4])
    lower_value = np.array([l_h, l_s, l_v])
    upper_value = np.array([u_h, u_s, u_v])

    mask= cv2.inRange(hsv,lower_value,upper_value)
    cv2.imshow("mask", mask)

    key=cv2.waitKey(1)
    if key==27:
        break
kernel = np.ones((5, 5), np.uint8)
mask= cv2.dilate(mask,kernel,iterations=15)
canny = cv2.Canny(mask, 100, 100)
cv2.imshow("canny",canny)
lines = cv2.HoughLines(canny, 0.7, np.pi/120, 120, min_theta=np.pi/36, max_theta=np.pi-np.pi/36)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 10000*(-b))
    y1 = int(y0 + 10000*(a))
    x2 = int(x0 - 10000*(-b))
    y2 = int(y0 - 10000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)


# Removing teh pixels that are above the horizon
m=(y2-y1)/(x2-x1)
c=y1-(m*x1)
print(c)
for i in range(x-1):
    for j in range(y-1):
        if 0 < (j*m+c)-i:
            img[i][j]=0

cv2.imshow("lined",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
