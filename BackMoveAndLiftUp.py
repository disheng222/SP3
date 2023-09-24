from hub import port
import runloop
import motor_pair, motor

async def main():
    # write your code here
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=-110)
    await motor.run_for_degrees(port.D, 270, 330)
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())
