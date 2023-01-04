import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('Park',img)

# Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x --> img to left
# -y --> up
# x --> right
# y --> down

translated = translate(img,-100,100)
cv.imshow('Translated',translated)

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45) # For anticlockwise specify negative value
cv.imshow('Rotated',rotated)

rotated_rotated = rotate(rotated,45)
cv.imshow('Roatated_rotated',rotated_rotated)

# Resizing

resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flipped',flip)
# 0 --> vertically
# 1 --> horizontally
# -2 --> both

# Cropping
cropped = img[200:400,300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)