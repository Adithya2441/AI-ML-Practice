import cv2 as cv


""" #read images using imread()
img = cv.imread('Photos/cat_large.jpg')
#show images in seperate window using imshow()
cv.imshow('Cat',img)

#wait for a key to be press 
cv.waitKey(0)
 """

#Reading Videos

#if we pass integers then we capture live video from webcam (0)
capture = cv.VideoCapture('Videos/dog.mp4')

#capture video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    #if d is pressed break
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#releases pointer
capture.release()
#destroys all windows
cv.destroyAllWindows()