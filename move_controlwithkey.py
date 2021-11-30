from djitellopy import Tello
import cv2

panel = cv2.imread('images.jpeg')
tello = Tello()

val = 50
i=0

tello.connect()

tello.streamon()
frame = tello.get_frame_read()

while 1:
    try:
        img = frame.frame

        cv2.namedWindow('tello stream')
        cv2.imshow('tello stream',img)

        k =cv2.waitKey(1) & 0xFF

        if k == ord('q'):
            break

        elif k== ord('p'):
            cv2.imwrite(f'picture{i}.png',img)
            i+=1

        elif k== ord('c'):
            val+=10

        elif k== ord('v'):
            val-=10

        elif k== ord('t'):
            tello.takeoff()

        elif k== ord('l'):
            tello.land()

        elif k== 82:
            tello.move_forward(val)

        elif k==84:
            tello.move_back(val)

        elif k==81:
            tello.move_left(val)

        elif k==83:
            tello.move_right(val)

        elif k== ord('w'):
            tello.flip_forward()

        elif k == ord('s'):
            tello.flip_back()

        elif k == ord('a'):
            tello.flip_left()

        elif k == ord('d'):
            tello.flip_right()

        elif k== ord('f'):
            tello.move_up(30)

        elif k== ord('g'):
            tello.move_down(30)

        elif k == ord('z'):
            tello.rotate_counter_clockwise(45)

        elif k == ord('x'):
            tello.rotate_clockwise(45)

        elif k == ord('e'):
            tello.emergency()

    except KeyboardInterrupt:
        tello.move_down(50)
        tello.land()

    except Exception as e:
        tello.move_down(50)
        tello.emergency()

    
tello.land()
tello.streamoff
cv2.destroyAllWindows()