from djitellopy import tello
import time
import KeyPressModule as kp
import cv2
kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()
global big_img
def getKeyboardInput():
    lr,fb,ud,yv = 0,0,0,0

    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): me.land(); time.sleep(3)

    if kp.getKey("e"): me.takeoff()

    if kp.getKey("z"): 
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg',big_img)
        time.sleep(0.3)
    
    if kp.getKey("1"): me.flip_forward()
    if kp.getKey("2"): me.flip_back()
    if kp.getKey("3"): me.flip_left()
    if kp.getKey("4"): me.flip_right()
    return [lr,fb,ud,yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    big_img = me.get_frame_read().frame
   
    img = cv2.resize(big_img,(360,240))
    cv2.imshow("Image",img)
    cv2.waitKey(1)
