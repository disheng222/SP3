from hub import port, motion_sensor
import runloop, motor, motor_pair
import time, distance_sensor

MIDDLE_WHEEL_MAX=1110 #The max speed value of MIDDLE WHEEL

def isDistanceLowerThan60():
    return distance_sensor.distance(port.E) < 70

async def main():
    # write your code here
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    motor_pair.move_tank(motor_pair.PAIR_1, -300, -400)
    await runloop.until(isDistanceLowerThan60)
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())

