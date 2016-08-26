import ev3dev.ev3 as ev3
import time


mediummm = ev3.MediumMotor('outC')
base = ev3.LargeMotor('outD')
hand = ev3.MediumMotor('outB')
naik = ev3.LargeMotor('outA')

touch = ev3.TouchSensor('in1')
distance = ev3.UltrasonicSensor('in2')
distance.mode = 'US-DIST-CM'
warna = ev3.ColorSensor('in4')
warna.mode = 'COL-COLOR'


def tekanKanan():
    while True:
        hand.run_forever(duty_cycle_sp=85, polarity="normal")
        print hand.position
        if hand.position > 220 :
            hand.stop()
            return

def balikKanan():
    while True:
        hand.run_forever(duty_cycle_sp=45, polarity="inversed")
        print hand.position
        if hand.position > 425 :
            hand.stop()
            return


def amikKanan():
    hand.reset()
    tekanKanan()
    time.sleep(2)
    balikKanan()
    while True:
        naik.run_forever(speed_sp=500, polarity='inversed')
        print "naik"
        if touch.value():
            print "sampaii"
            naik.stop()
            break
    return

def tekanKiri():
    while True:
        hand.run_forever(duty_cycle_sp=85, polarity="inversed")
        print hand.position
        if hand.position > 220 :
            hand.stop()
            return

def balikKiri():
    while True:
        hand.run_forever(duty_cycle_sp=45, polarity="normal")
        print hand.position
        if hand.position > 425 :
            hand.stop()
            return

def amikKiri():
    hand.reset()
    tekanKiri()
    time.sleep(2)
    balikKiri()
    while True:
        naik.run_forever(speed_sp=500, polarity='inversed')
        print "naik"
        if touch.value():
            print "sampaii"
            naik.stop()
            break
    return



def move(current_hole):
    if current_hole == 0 :
        if distance.value() < 32 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 32 :
                    base.stop()
                    amikKanan()
                    return
        if distance.value() > 32 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() < 32 :
                    base.stop()
                    amikKanan()
                    return

    if current_hole == 1 :
        if distance.value() < 166:
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 166:
                    base.stop()
                    hand.reset()
                    amikKanan()
                    return

        if distance.value() > 166:
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() > 166:
                    base.stop()
                    hand.reset()
                    amikKanan()
                    return

    if current_hole == 2 :
        if distance.value() < 325 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 325:
                    base.stop()
                    amikKanan()
                    return
        else :
                amikKanan()
                return

    if current_hole == 4 :
        if distance.value() < 325 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 325:
                    base.stop()
                    amikKiri()
                    return
        else :
            amikKiri()
            return

    if current_hole == 5 :
        if distance.value() > 166:
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() < 166:
                    base.stop()
                    amikKiri()
                    return
        if distance.value() < 166:
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 166:
                    base.stop()
                    amikKiri()
                    return

    if current_hole == 6 :
        if distance.value() > 32 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() < 32:
                    base.stop()
                    amikKiri()
                    return
        else :
            amikKiri()
            return


print distance.value()
current_hole = int(raw_input("Nak amik bola kat mana?"))
move(current_hole)
