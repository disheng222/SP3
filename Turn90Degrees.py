import motor_pair
from hub import port, light_matrix
from hub import motion_sensor
import runloop

async def main():
    # write your code here
    await light_matrix.write("Hi!")
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    #turn left 90 degrees
    while motion_sensor.tilt_angles()[0]<900:
        motor_pair.move(motor_pair.PAIR_1, -100)
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())
