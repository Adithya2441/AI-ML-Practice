import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape,dtype = 'uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)
#we are thresholding the image to binary format using the lower 125 thresh and upper 255

contours, hierarchies = cv.findContours(canny , cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# we pass edges , RETR_LIST returns us the entire list of contours (also has RETR_EXTERNAL and _TREE)
# and CHAIN_APPROX how we want to approx the contours Has NONE and SIMPLE 
# None gives all points of contours but Simple gives only the endpoints of the lines
print(f'{len(contours)} contour(s) found!')
#blurring can reduce contours

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("Contours Drawn",blank)
#draw contours draws the contours on the blank img 
# we pass contours and -1 to get all the contours we pass a color and then thickness of the lines

cv.waitKey(0)
