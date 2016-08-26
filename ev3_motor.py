from ev3dev.auto import *

m = LargeMotor('outA')
mediumm = MediumMotor('outC')
m.run_timed(time_sp=500, duty_cycle_sp=75)
mediumm.run_timed(time_sp=100, duty_cycle_sp=75)
print "yes"

import touch_stop
