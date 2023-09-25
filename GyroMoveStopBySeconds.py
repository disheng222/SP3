from hub import port, motion_sensor
import runloop, motor, motor_pair
import time

MIDDLE_WHEEL_MAX=1110 #The max speed value of MIDDLE WHEEL

#equivalent get_yaw_angle() in SP2
def get_yaw_angle():
    return (int)(-motion_sensor.tilt_angles()[0]*0.1)

#gyrostraight
#motorPair: the motor pair defined beforehand
#direction: the direction the robot will move toward
#speed: the speed value (-100,100)
#seconds: the time to move in seconds (could be a float)
def gyroMoveStopbySeconds(motorPair, direction, speed, seconds):
    milliseconds = seconds*1000
    v = (int)(speed*MIDDLE_WHEEL_MAX/100)
    if(speed>0):
        start = time.ticks_ms()
        while True:
            if(time.ticks_diff(time.ticks_ms(), start) > milliseconds):
                motor_pair.stop(motorPair)
                break
            motor_pair.move(motorPair, 2*(direction-get_yaw_angle()), velocity=v)
    else:
        start = time.ticks_ms()
        while True:
            if(time.ticks_diff(time.ticks_ms(), start) > milliseconds):
                motor_pair.stop(motorPair)
                break
            motor_pair.move(motorPair, -2*(direction-get_yaw_angle()), velocity=v)        


async def main():
    # write your code here
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    motion_sensor.reset_yaw(0)
    await runloop.until(motion_sensor.stable)
    gyroMoveStopbySeconds(motor_pair.PAIR_1, 0, 30, 2)
    gyroMoveStopbySeconds(motor_pair.PAIR_1, -45, 30, 2)
    gyroMoveStopbySeconds(motor_pair.PAIR_1, -90, 30, 2)
    gyroMoveStopbySeconds(motor_pair.PAIR_1, -90, -30, 2)
    gyroMoveStopbySeconds(motor_pair.PAIR_1, -45, -30, 2)
    gyroMoveStopbySeconds(motor_pair.PAIR_1, 0, -30, 2)

runloop.run(main())



