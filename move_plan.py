from djitellopy import Tello
import cv2

tello = Tello()

tello.connect()
tello.takeoff()

while 1:
    try:
        cv2.namedWindow('a')
        k =cv2.waitKey(1) & 0xFF
        print(k)
        if k == ord('q'):
            break
        elif k== 82:
            tello.move_forward(90)

        elif k==ord('s'):
            tello.move_back(90)

        elif k==ord('a'):
            tello.move_left(90)

        elif k==ord('d'):
            tello.move_right(90)


        elif k== ord('f'):
            tello.flip_forward()

        elif k == ord('g'):
            tello.flip_back()

        elif k== ord('e'):
            tello.move_up(30)

        elif k== ord('r'):
            tello.move_down(30)
        elif k == 82:
            tello.query_attitude({'t'})

    except KeyboardInterrupt:
        tello.move_down(50)
        tello.land()

    except Exception as e:
        tello.move_down(50)
        tello.emergency()

tello.move_down(50)
tello.land()
cv2.destroyAllWindows()