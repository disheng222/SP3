from hub import port, motion_sensor
import runloop, motor, motor_pair, math

motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
MIDDLE_WHEEL_MAX=1110 #The max speed value of MIDDLE WHEEL

#equivalent get_yaw_angle() in SP2
def get_yaw_angle():
    return (int)(-motion_sensor.tilt_angles()[0]*0.1)

#gyrostraight
#motorPair: the motor pair defined beforehand
#direction: the direction the robot will move toward
#speed: the speed value (-100,100)
#relpos: the amount of relative position you want to move
def GyroMoveStopbyRelativePosition(motorPair, direction, speed, relpos):
    motor.reset_relative_position(motorPair, 0)
    v = (int)(speed*MIDDLE_WHEEL_MAX/100)
    if(speed>0):
        while True:
            if abs(motor.relative_position(motorPair)) > relpos:
                motor_pair.stop(motorPair)
                break
            motor_pair.move(motorPair, 2*(direction-get_yaw_angle()), velocity=v)
    else:
        while True:
            if motor.relative_position(motorPair) > relpos:
                motor_pair.stop(motorPair)
                break
            motor_pair.move(motorPair, -2*(direction-get_yaw_angle()), velocity=v)


async def main():
    GyroMoveStopbyRelativePosition(motor_pair.PAIR_1, 0, 10, 550)

runloop.run(main())
