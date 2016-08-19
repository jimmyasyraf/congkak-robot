#! /usr/bin/env python

import random
import sys
import time


import ev3dev.ev3 as ev3

############# DECLARE SERVO AND MOTORS ###########################

#MOTORS
naik = ev3.LargeMotor('outA')
hand = ev3.MediumMotor('outB')
mediummm = ev3.MediumMotor('outC')
base = ev3.LargeMotor('outD')

#SENSORS
touch = ev3.TouchSensor('in1')

distance = ev3.UltrasonicSensor('in2')
distance.mode = 'US-DIST-CM' #the measured unit is actually in mm

hand_distance = ev3.InfraredSensor('in3')
hand_distance.mode = 'IR-PROX'

warna = ev3.ColorSensor('in4')
warna.mode = 'COL-COLOR'

##################################################################

######### CHECK WHICH HOLE HUMAN TAKES FROM ##################

def check_hole():
    time.sleep(2)
    if hand_distance.value() < 20 :
        chosen_hole = 2
    if hand_distance.value() > 20 and hand_distance.value() < 50 :
        chosen_hole = 1
    if hand_distance.value() > 51 :
        chosen_hole = 0
    return chosen_hole

#############################################


######## ROBOT'S MOVEMENTS TO THE SPECIFIC HOLE AND TAKE BALL ###########

def tekanKanan():
    while True:
        hand.run_forever(duty_cycle_sp=85, polarity="normal")
        #print hand.position
        if hand.position > 220 :
            hand.stop()
            return

def balikKanan():
    while True:
        hand.run_forever(duty_cycle_sp=45, polarity="inversed")
        #print hand.position
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
        #print hand.position
        if hand.position > 220 :
            hand.stop()
            return

def balikKiri():
    while True:
        hand.run_forever(duty_cycle_sp=45, polarity="normal")
        #print hand.position
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



def take_ball(current_hole):
    if current_hole == 0 :
        if distance.value() < 32 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 32 :
                    base.stop()
                    amikKanan()
                    time.sleep(3)
                    return
        if distance.value() > 32 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() < 32 :
                    base.stop()
                    amikKanan()
                    time.sleep(3)
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
                    time.sleep(3)
                    return

        if distance.value() > 166:
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() > 166:
                    base.stop()
                    hand.reset()
                    amikKanan()
                    time.sleep(3)
                    return

    if current_hole == 2 :
        if distance.value() < 320 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 320:
                    base.stop()
                    amikKanan()
                    time.sleep(3)
                    return
        else :
                amikKanan()
                time.sleep(3)
                return

    if current_hole == 4 :
        if distance.value() < 320 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 320:
                    base.stop()
                    amikKiri()
                    time.sleep(3)
                    return
        else :
            amikKiri()
            time.sleep(3)
            return

    if current_hole == 5 :
        if distance.value() > 166:
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() < 166:
                    base.stop()
                    amikKiri()
                    time.sleep(3)
                    return
        if distance.value() < 166:
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 166:
                    base.stop()
                    amikKiri()
                    time.sleep(3)
                    return

    if current_hole == 6 :
        if distance.value() > 32 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='normal')
                print distance.value()
                if distance.value() < 32:
                    base.stop()
                    amikKiri()
                    time.sleep(3)
                    return
        else :
            amikKiri()
            time.sleep(3)
            return

############################################################


##### ROBOT'S MOVEMENTS TO THE NEXT HOLE AND DISTRIBUTE BALL ############



def letakKiri() :
    while True:
        mediummm.run_forever(duty_cycle_sp=70,polarity='inversed')
        print mediummm.position
        if mediummm.position > 120 :
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
        if mediummm.position > 120 :
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
        if distance.value() < 320 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 320:
                    base.stop()
                    sort_ball_right()
                    return
        else :
                sort_ball_right()
                return

    if current_hole == 4 :
        if distance.value() < 320 :
            while True:
                base.run_forever(duty_cycle_sp=85, polarity='inversed')
                print distance.value()
                if distance.value() > 320:
                    base.stop()
                    sort_ball_left()
                    return
        else :
            sort_ball_left()
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

############################################################

############## ACTUAL GAMEPLAY ############################

hole = [4,4,4,0,4,4,4,0]

def start():
    print ""
    print "WELCOME TO CONGKAK!"
    print ""
    while True:
        base.run_forever(duty_cycle_sp= 85, polarity = 'normal')
        if distance.value() < 32 :
            base.stop()
            print "Press the touch sensor and select new hole (0,1,2)"
            break


current_player = 1

round_number = 1

def main_game():
    global current_player
    global hole
    print "Player %d" % current_player
    if current_player == 1:
        if hole[0] != 0 or hole[1] != 0 or hole[2] != 0 :
            chosen = check_hole() #see distance to hand and guess which hole picked
            if chosen == 0 or chosen == 1 or chosen == 2:
                distribute_balls(chosen)
            else:
                main_game()
        else :
            print "No balls Human side"
            current_player = 2
            print "Press the touch sensor to continue"
            while True:
                if touch.value() :
                    main_game()

    if current_player == 2:
        if hole[4] != 0 or hole[5] != 0 or hole[6] != 0 :
            #chosen = int(raw_input("Choose which hole (4,5,6): "))
            chosen = random.randint(4,6)
            if chosen == 4 or chosen == 5 or chosen == 6:
                if hole[chosen] != 0 :
                    distribute_balls(chosen)
                else:
                    main_game()
        else :
            print "No more balls on Robot side"
            current_player = 1
            print "Press the touch sensor to continue"
            while True:
                if touch.value() :
                    main_game()


def distribute_balls(chosen):
    global round_number
    global current_player
    print "Round %d" % round_number
    global hole

    current_hole = chosen
    distribute = hole[chosen]
    balls_in_hand = hole[chosen]

    if current_player == 2 :
        take_ball(chosen)

    print "Chosen hole: %d" % current_hole
    print "# balls in hand: %d" % distribute
    if balls_in_hand == 0:
        if current_player == 1:
            current_player = 2
            print "No balls left for HUMAN"
            #print "Next player: %d" % current_player
            print "Next player: ROBOT"
            print "Press the touch sensor to continue"
            while True:
                if touch.value() :
                    main_game()

        if current_player == 2:
            current_player = 1
            print "No balls left for ROBOT"
            #print "Next player: %d" % current_player
            print "Next player: HUMAN"
            print "Press the touch sensor to continue"
            while True:
                if touch.value() :
                    main_game()
    hole[chosen] = 0  #take all the ball inside
    while balls_in_hand != 0:
    #for x in range(0,distribute):
        #print x
        next_hole = current_hole + 1
        current_hole = next_hole
        if current_hole == 8: #cycle back to hole number 0
            current_hole = 0
        if current_player == 1:
            if next_hole != 7: #the enemy hole! dont put in
                hole[current_hole] = hole[current_hole] + 1 #else, put 1 in
                balls_in_hand = balls_in_hand - 1
        if current_player == 2:
            if next_hole != 3: #the enemy hole! dont put in
                move(current_hole)
                hole[current_hole] = hole[current_hole] + 1 #else, put 1 in
                balls_in_hand = balls_in_hand - 1

        #print "Hole %d: %d" % (current_hole, hole[current_hole])


        if balls_in_hand == 0:
        #if x == (distribute-1):
            print " "
            print "        Hole 7: %d" % hole[7]
            print " "
            print "Hole 6: %d        Hole 0: %d" % (hole[6], hole[0])
            print " "
            print "Hole 5: %d        Hole 1: %d" % (hole[5], hole[1])
            print " "
            print "Hole 4: %d        Hole 2: %d" % (hole[4], hole[2])
            print " "
            print "        Hole 3: %d" % hole[3]
            print " "
            next_round_number = round_number + 1
            round_number = next_round_number
            total_balls = hole[0]+hole[1]+hole[2]+hole[3]+hole[4]+hole[5]+hole[6]+hole[7]
            print "Total balls: %d" % total_balls
            print "Last hole: %d" % current_hole
            print " "
            if (hole[0] == 0 and hole[1] == 0 and hole[2] == 0 and hole[4] == 0 and hole[5] == 0 and hole[6] == 0):
                if hole[3] > hole[7]:
                    print "HUMAN WINS !"
                    sys.exit()
                    break
                if hole[7] > hole[3]:
                    print "ROBOT WINS !"
                    sys.exit()
                    break
                if hole[3] == hole[7]:
                    print "It's a tie"
                    sys.exit()
                    break

            if ((current_hole==0 or current_hole==1 or current_hole==2 or current_hole==4 or current_hole==5 or current_hole==6) and hole[current_hole] == 1):
                print "PLAYER %d DIE!" % current_player
                if current_player == 1:
                    current_player = 2
                    print "Next player: %d" % current_player
                    print "Press the touch sensor to continue"
                    while True:
                        if touch.value() :
                            main_game()
                if current_player == 2:
                    current_player = 1
                    print "Next player: %d" % current_player
                    print "Press the touch sensor to continue"

                    while True:
                        if touch.value() :
                            main_game()
            home(current_hole)

def home(current_hole):
    if current_player == 1:
        if (current_hole==3):
            print "You are stopping at home."
            print "Press the touch sensor and select new hole (0,1,2)"
            #current_hole = random.randint(0,2)
            while True:
                if touch.value() :

                        time.sleep(3)
                        new_hole = check_hole()
                        #new_hole = int(raw_input(""))
                        if new_hole == 0 or new_hole == 1 or new_hole == 2 :
                            distribute_balls(new_hole)
                        else:
                            print "Not holes from your side"
                            print " "
                            home(current_hole)
        distribute_balls(current_hole)

    if current_player == 2:
        if (current_hole==7):
            print "Robot stopped at home. Selecting new hole (4,5,6) ...."
            #current_hole = random.randint(0,2)
            new_hole = random.randint(4,6)
            if new_hole == 4 or new_hole == 5 or new_hole == 6 :
                distribute_balls(new_hole)
            else:
                print "Not holes from your side"
                print " "
                home(current_hole)
        distribute_balls(current_hole)

################################################################

start()
while True:
    if touch.value() :
        main_game()
