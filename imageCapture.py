from djitellopy import tello
import cv2

#create a tello obj and connect drone
me = tello.Tello()
me.connect()
print(me.get_battery())

me.stream_on()

while True:
    img = me.get_frame_read().frame
    
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Img", img)
    cv2.waitKey(1)