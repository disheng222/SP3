from hub import port, motion_sensor
import runloop, motor, motor_pair
import time, color_sensor

MIDDLE_WHEEL_MAX=1110 #The max speed value of MIDDLE WHEEL

#equivalent get_yaw_angle() in SP2
def get_yaw_angle():
    return (int)(-motion_sensor.tilt_angles()[0]*0.1)

#gyrostraight
#motorPair: the motor pair defined beforehand
#colorPort: the port connected by the color sensor
#direction: the direction the robot will move toward
#speed: the speed value (-100,100)
def gyroMoveStopbyBlackLine(motorPair, colorPort, direction, speed):   
    v = (int)(speed*MIDDLE_WHEEL_MAX/100)
    if(speed > 0):
        while True:
            if(color_sensor.reflection(colorPort) < 50):
                motor_pair.stop(motorPair)
                break
            motor_pair.move(motorPair, 2*(direction-get_yaw_angle()), velocity=v)
    else:
        while True:
            if(color_sensor.reflection(colorPort) < 50):
                motor_pair.stop(motorPair)
                break
            motor_pair.move(motorPair, -2*(direction-get_yaw_angle()), velocity=v)


async def main():
    # write your code here
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    motion_sensor.reset_yaw(0)
    await runloop.until(motion_sensor.stable)

    #move along the direction -44 degrees with the speed 30% and stop at the black line
    gyroMoveStopbyBlackLine(motor_pair.PAIR_1, port.F, -44, 30)

runloop.run(main())



