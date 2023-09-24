from hub import port, motion_sensor
import runloop, motor, motor_pair
import time

MIDDLE_WHEEL_MAX=1110#The max speed value of MIDDLE WHEEL

#equivalent get_yaw_angle() in SP2
def get_yaw_angle():
    return (int)(-motion_sensor.tilt_angles()[0]*0.1)

def gyrostraight(motorPair, speed, seconds):
    milliseconds = seconds*1000
    v = (int)(speed*MIDDLE_WHEEL_MAX/100)
    motion_sensor.reset_yaw(0)
    start = time.ticks_ms()
    while True:
        if(time.ticks_diff(time.ticks_ms(), start) > milliseconds):
            motor_pair.stop(motorPair)
            break

        motor_pair.move(motorPair, -2*get_yaw_angle(), velocity=v)


async def main():
    # write your code here
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    gyrostraight(motor_pair.PAIR_1, 30, 3)

runloop.run(main())

