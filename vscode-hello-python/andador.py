#!/usr/bin/env python3
#!/usr/bin/env python3
from ev3dev.motor import LargeMotor, OUTPUT_A, OUTPUT_B, LargeMotor, MoveSteering
from ev3dev.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep

lm1 = LargeMotor(OUTPUT_A)
lm2 = LargeMotor(OUTPUT_B)
lm1.on_for_seconds(speed = 50, seconds=3)
lm2.on_for_seconds(speed = 50, seconds=3)
sleep(1)
lm1.on_for_seconds(speed = 50, seconds=3)
sleep(1)
lm2.on_for_seconds(speed = 50, seconds=3)
sleep(1)
steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
steer_pair.on_for_seconds(steering=-100, speed=50, seconds=2)

