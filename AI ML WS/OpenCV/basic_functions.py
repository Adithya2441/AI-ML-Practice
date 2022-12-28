import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Park',img)

# Converting image to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
# second parameter is the kernel which is a 2,2 tuple
# it is a matrix used by GaussianBlur to blur the img
# it has to be an odd number
# increase the values to increase the amt of blur

# Edge Cascade
canny = cv.Canny(blur, 125 ,175)
cv.imshow('Canny Edges',canny)
# if we blur the img it reduces the edges in the img
# greater the blur lesser the edges

# Dilating the img
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

# Eroding
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)
#erode is used to retrieve the image after dilation
#it may not be as perfect as the original

# Resize
resize = cv.resize(img, (500,500) , interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resize)
# resizes the img without maintaining aspect ratio
# we pass the required height and width
# INTER_AREA is used while reducing the size
# INTER_LINEAR or INTER_CUBIC used while increasing size
# CUBIC is the slowest but has a higher quality

# Croping
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)
# we pass in the dimensions to be displayed

cv.waitKey(0)