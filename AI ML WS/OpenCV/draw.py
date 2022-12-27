import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype = 'uint8')
#(width,height,color_channels)
cv.imshow('Blank',blank)
#uint8 is the image datatype

# 1.Paint the image a certain color
blank[200:300,300:400] = 255,0,0
cv.imshow('Blue',blank)

# 2.Draw a Rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
#thickness can be given as -1 to fill or any int for border only
cv.imshow('Rectangle',blank)

# 3.Draw a cirlce
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)

# 4.Draw a line
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
cv.imshow('Line',blank)

# 5.Write text on an image
cv.putText(blank,'Hello',(225,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)