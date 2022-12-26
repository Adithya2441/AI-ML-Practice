import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    #frame.shape has height at index 1 and width at index 0
    #Works for imgs vids and live vids
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #works only for Live Video
    capture.set(3,width)
    capture.set(4,height)


img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)
resized_img = rescaleFrame(img)
cv.imshow('Cat_Resized',resized_img)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=0.2)

    cv.imshow('Video',frame)
    cv.imshow('Video_Resized',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()