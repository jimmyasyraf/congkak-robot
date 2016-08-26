import ev3dev.ev3 as ev3
import time


mediummm = ev3.MediumMotor('outC')
base = ev3.LargeMotor('outD')

distance = ev3.UltrasonicSensor('in2')
distance.mode = 'US-DIST-CM'
warna = ev3.ColorSensor('in4')
warna.mode = 'COL-COLOR'



def letakKiri() :
    while True:
        mediummm.run_forever(duty_cycle_sp=70,polarity='inversed')
        print mediummm.position
        if mediummm.position > 130 :
            mediummm.stop()
            return

def centerKiri() :
    while True:
        mediummm.run_forever(duty_cycle_sp=60, polarity="normal")
        print warna.value()
        if warna.value() == 1:
            mediummm.stop()
            return

def sort_ball_left():
    mediummm.reset()
    letakKiri()
    time.sleep(1)
    centerKiri()
    return

def letakKanan() :
    while True:
        mediummm.run_forever(duty_cycle_sp=70,polarity='normal')
        print mediummm.position
        if mediummm.position > 130 :
            mediummm.stop()
            return

def centerKanan() :
    while True:
        mediummm.run_forever(duty_cycle_sp=60, polarity="inversed")
        print warna.value()
        if warna.value() == 1:
            mediummm.stop()
            return

def sort_ball_right():
    mediummm.reset()
    letakKanan()
    time.sleep(1)
    centerKanan()
    return


def move(current_hole):
    if current_hole == 0 :
        if distance.value() < 60 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 60 :
                    base.stop()
                    sort_ball_right()
                    return
        if distance.value() > 60 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() < 60 :
                    base.stop()
                    sort_ball_right()
                    return

    if current_hole == 1 :
        if distance.value() < 230:
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 230:
                    base.stop()
                    sort_ball_right()
                    return
        if distance.value() > 230:
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() > 230:
                    base.stop()
                    sort_ball_right()
                    return

    if current_hole == 2 :
        if distance.value() < 325 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 325:
                    base.stop()
                    sort_ball_right()
                    return
        else :
                sort_ball_right()
                return

    if current_hole == 4 :
        if distance.value() < 325 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 325:
                    base.stop()
                    sort_ball_left()
                    return
        else :
            sort_ball_right()
            return

    if current_hole == 5 :
        if distance.value() > 230:
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() < 230:
                    base.stop()
                    sort_ball_left()
                    return
        if distance.value() < 230:
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 230:
                    base.stop()
                    sort_ball_left()
                    return

    if current_hole == 6 :
        if distance.value() > 60 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() < 60:
                    base.stop()
                    sort_ball_left()
                    return
        if distance.value() < 60 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 60:
                    base.stop()
                    sort_ball_left()
                    return

    if current_hole == 7 :
        if distance.value() > 32 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() < 32:
                    base.stop()
                    sort_ball_left()
                    return
        else :
            sort_ball_left()
            return

print distance.value()
current_hole = int(raw_input("Nak gi lubang mana?"))
move(current_hole)

'''

def sort_ball_left():
    mediummm.run_timed(speed_sp=60, time=800, polarity="inversed")
    time.sleep(1)
    #print warna.value()
    while True:
        mediummm.run_forever(speed_sp=50, polarity="normal")
        print warna.value()
        if warna.value() == 1:
            mediummm.stop()
            break

def sort_ball_right():
    mediummm.run_timed(speed_sp=60, time=800, polarity="normal")
    time.sleep(1)
    #print warna.value()
    while True:
        mediummm.run_forever(speed_sp=50, polarity="inversed")
        print warna.value()
        if warna.value() == 1:
            mediummm.stop()
            break

'''
