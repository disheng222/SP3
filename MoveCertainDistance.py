from hub import light_matrix, port
import motor_pair
import runloop
import motor

WHEEL_CIRCUMFERENCE = 17.5 # cm, this is a constant for your robot
def degreesForDistance(distance_cm): # input must be in the same unit as WHEEL_CIRCUMFERENCE
    return int((distance_cm/WHEEL_CIRCUMFERENCE) * 360) # Add multiplier for gear ratio if needed

async def main():
    # write your code here
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    #move the robot 20cm.
    motor_pair.move_for_degrees(motor_pair.PAIR_1, degreesForDistance(20), 0, velocity = 400, stop = motor.HOLD)

runloop.run(main())
