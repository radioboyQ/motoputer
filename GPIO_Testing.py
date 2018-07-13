#!/bin/python3

import asyncio
from signal import pause
import time

from gpiozero.pins.pigpio import PiGPIOFactory
import gpiozero

factory = PiGPIOFactory()

color_pin_dict = {"Red": 16, "Blue": 20, "Green": 21} #, "Norm_Closed": 19}
gps_button_pin_dict = {"Sensor": 26}
running = True

# Set up LED in global space so callbacks can use it
gps_btn_led = gpiozero.RGBLED(color_pin_dict["Red"], color_pin_dict["Green"], color_pin_dict["Blue"], active_high=False, initial_value=(0, 0, 0), pwm=True, pin_factory=factory)

# Callbacks
def gps_btn_callback():
    print("Button pressed")
    # Purple
    gps_btn_led.color = .3, 0, .5

# ToDo: Add poweroff callback


async def main():
    try:
        # Button setup
        gps_btn = gpiozero.Button(gps_button_pin_dict["Sensor"])
        gps_btn.when_pressed = gps_btn_callback



        # Green
        gps_btn_led.color = 0, 1, 0

        while running:
            await asyncio.sleep(15)
            # Check GPS's status
            gps_btn_led.color = 0, 1, 0

    except KeyboardInterrupt:
        # gps_btn_led.color = (0, 0, 0)
        print("[!] Keyboard interrupt caught!")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()