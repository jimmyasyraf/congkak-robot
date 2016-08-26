#make sure battery 7.25

import ev3dev.ev3 as ev3
import time

touch = ev3.TouchSensor('in1')
m = ev3.LargeMotor('outA')
mediummm = ev3.MediumMotor('outC')
warna = ev3.ColorSensor('in4')
warna.mode = 'COL-COLOR'

def sort_ball_left():
    mediummm.run_timed(duty_cycle_sp=70, time=1200, polarity="normal")
    time.sleep(1)
    #print warna.value()
    while True:
        mediummm.run_forever(duty_cycle_sp=40, polarity="inversed")
        print warna.value()
        if warna.value() == 1:
            mediummm.stop()
            break

def sort_ball_right():
    mediummm.run_timed(duty_cycle_sp=70, time=1200, polarity="inversed")
    time.sleep(1)
    #print warna.value()
    while True:
        mediummm.run_forever(duty_cycle_sp=40, polarity="normal")
        print warna.value()
        if warna.value() == 1:
            mediummm.stop()
            break

def which_side():
    kirikanan = int(raw_input("Kiri (1) ke kanan (2) ?"))
    if kirikanan == 1:
        sort_ball_left()
    if kirikanan == 2:
        sort_ball_right()

while True:
    m.run_forever(speed_sp=500, polarity='inversed')
    print "naik"
    if touch.value():
        print "sampaii"
        m.stop()
        break
