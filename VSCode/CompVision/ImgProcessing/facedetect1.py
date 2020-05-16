"""
This script is used to detect faces.
"""

from cv2 import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("news.jpg")
#  Converts bgr img to gray.
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1,
minNeighbors=5)

print(faces)  #  it will return ndim array which specifies the face area pixel numbers.

#  to print rectangle around the face using coordinates in faces variable.
for x,y,h,w in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)


cv2.imshow("keanu",img)
cv2.waitKey(0)
cv2.destroyAllWindows()