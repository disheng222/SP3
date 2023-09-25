from hub import port, motion_sensor
import runloop, motor, motor_pair
import time, distance_sensor

MIDDLE_WHEEL_MAX=1110 #The max speed value of MIDDLE WHEEL

#equivalent get_yaw_angle() in SP2
def get_yaw_angle():
    return (int)(-motion_sensor.tilt_angles()[0]*0.1)

#gyrostraight
#motorPair: the motor pair defined beforehand
#disPort: the port connected by the distance sensor
#direction: the direction the robot will move toward
#speed: the speed value (-100,100)
#distance: when the distance is smaller than this number (masured in millimeters), the robot will stop
def gyroMoveStopbyDistance(motorPair, disPort, direction, speed, target_distance):
    distance = target_distance
    v = (int)(speed*MIDDLE_WHEEL_MAX/100)
    if(speed > 0):
        while True:
            current_distance = distance_sensor.distance(disPort)
            if(current_distance==-1):
                continue
            if(current_distance < distance):
                motor_pair.stop(motorPair)
                break
            motor_pair.move(motorPair, 2*(direction-get_yaw_angle()), velocity=v)
    else:
        while True:
            current_distance = distance_sensor.distance(disPort)
            if(current_distance==-1):
                continue          
            if(current_distance < distance):
                motor_pair.stop(motorPair, )
                break
            motor_pair.move(motorPair, -2*(direction-get_yaw_angle()), velocity=v)


async def main():
    # write your code here
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    motion_sensor.reset_yaw(0)
    await runloop.until(motion_sensor.stable)

    #move along the direction -44 degrees with the speed 30% and stop at the black line
    gyroMoveStopbyDistance(motor_pair.PAIR_1, port.E, 0, -30, 60)

runloop.run(main())



