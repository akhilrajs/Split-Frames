import cv2
import os

name_of_file = input("enter file name :> ")
# Playing video from file:
cap = cv2.VideoCapture(name_of_file)
dest = "frames_of_" + str(name_of_file)
try:
    if not os.path.exists(dest):
        os.makedirs(dest)
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './frames/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
