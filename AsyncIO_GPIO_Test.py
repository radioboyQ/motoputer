import asyncio
import RPi.GPIO as GPIO

# Source: https://raspberrypi.stackexchange.com/a/56454

BTN_IN = 16
# LOOP_OUT = 22

# @asyncio.coroutine
# def delayed_raise_signal():
#     yield from asyncio.sleep(1)
#     print("Button push detected!")
#     print("Adding current location to database")

@asyncio.coroutine
def stop_loop():
    yield from asyncio.sleep(1)

    print('Stopping Event Loop')
    asyncio.get_event_loop().stop()
    print("Exiting!")
    GPIO.cleanup()

def gpio_event_on_loop_thread():
    print("[*] Threadsafe function.")
    print("[*] Adding current location to database")
    # asyncio.async(stop_loop())

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BTN_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def on_gpio_event(channel):
        loop.call_soon_threadsafe(gpio_event_on_loop_thread)

    loop = asyncio.get_event_loop()
    GPIO.add_event_detect(BTN_IN, GPIO.RISING, callback=on_gpio_event, bouncetime=2000)
    asyncio.sleep(1)

if __name__ == '__main__':
    setup()
    try:
        print("Starting!")
        asyncio.get_event_loop().run_forever()
    except:
        print("Exiting!")
        GPIO.cleanup()