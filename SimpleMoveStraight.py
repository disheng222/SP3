from hub import port
import runloop
import motor_pair

async def main():
    # Pair motors on port A and B
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    await runloop.sleep_ms(2000) #sleep 2s

    # Move straight at default velocity
    motor_pair.move(motor_pair.PAIR_1, 0)

    await runloop.sleep_ms(2000)

    # Move straight at a specific velocity
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=280)

    await runloop.sleep_ms(2000)

    # Move straight at a specific velocity and acceleration
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=280, acceleration=100)

runloop.run(main())

