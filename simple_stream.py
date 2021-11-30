from djitellopy import Tello
import cv2

tello = Tello()

tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()
while 1:
    try:
        cv2.imshow('tello stream',frame_read.frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    except:
        pass

tello.streamoff()

pass