import cv2
import numpy as np
import face_recognition

imgRohit = face_recognition.load_image_file('images/Rohit.jpg')
imgRohit = cv2.cvtColor(imgRohit.cv2.COLOR_BGR2RGB)
imgRohit_1 = face_recognition.load_image_file('images/Rohit_1.jpg')
imgRohit_1 = cv2.cvtColor(imgRohit_1.cv2.COLOR_BGR2RGB)

cv.imshow('Rohit', imgRohit)
cv.imshow('Rohit_1', imgRohit_1)
cv.waitKey(0)
