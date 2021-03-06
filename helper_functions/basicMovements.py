from djitellopy import tello
from time import sleep

#create a tello obj and connect drone
me = tello.Tello()
me.connect()
print(me.get_battery())

#test code for takeoff
me.takeoff()
me.send_rc_control(0, 50, 0, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
me.land()
me.move_forward()
