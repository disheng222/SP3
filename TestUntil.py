from hub import port
import color_sensor
import color
import runloop

def is_color_red():
    return color_sensor.color(port.F) is color.RED

async def main():
    # Wait until Color Sensor sees red
    await runloop.until(is_color_red)
    print("Red!")

runloop.run(main())
