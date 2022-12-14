import cv2 as cv


#read images using imread()
#pass the path of the img
img = cv.imread('Photos/cat_large.jpg')
#show images in seperate window using imshow()
#pass window name and the img
cv.imshow('Cat',img)

#wait for a key to be press 
cv.waitKey(0)


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

    #Gives error as the frames end after a point
    #python cant find any more frames in that loc

#releases pointer
capture.release()
#destroys all windows
cv.destroyAllWindows()