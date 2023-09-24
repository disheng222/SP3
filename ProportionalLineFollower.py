from hub import motion_sensor, port
import runloop
import color_sensor, motor_pair, time

MIDDLE_WHEEL_MAX=1110 #The max speed value of MIDDLE WHEEL
LINE_FOLLOW_LEFT_EDGE=0
LINE_FOLLOW_RIGHT_EDGE=1

#follow black line based on proportional line following algorithm
#motorPair: e.g., motor_pair.PAIR_1
#colorPort: e.g., port.F
#mode: either LINE_FOLLOW_LEFT_EDGE or LINE_FOLLOW_RIGHT_EDGE
#speed: a number in (0,100]
#seconds: could be a floating/decimal, such as 2.5
def proportionalLineFollower(motorPair, colorPort, mode, speed=20, seconds=2):
    milliseconds = seconds*1000
    v = (int)(speed*MIDDLE_WHEEL_MAX/100)
    color_sensor.color(colorPort)
    start = time.ticks_ms()
    steering = 0
    while(True):
        if(time.ticks_diff(time.ticks_ms(), start) > milliseconds):
            motor_pair.stop(motorPair)
            break
        if(mode==0): #follow left edge
            steering = (color_sensor.reflection(colorPort)-60)
        else: #follow right edge
            steering = (60-color_sensor.reflection(colorPort))
        
        #move the robot
        motor_pair.move(motorPair, steering, velocity=v)

async def main():
    # write your code here
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    proportionalLineFollower(motor_pair.PAIR_1, port.F, LINE_FOLLOW_RIGHT_EDGE, 20, 20)

runloop.run(main())

