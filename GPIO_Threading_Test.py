import RPi.GPIO as GPIO
import threading
import time
import random

from multiprocessing import Pool

R = 16
G = 21
B = 20

PINS = [R, G, B]

_FINISH = False

def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)


def color_test(channel, frequency, speed, step):
    p = GPIO.PWM(channel, frequency)
    p.start(0)
    while True:
        for dutyCycle in range(0, 101, step):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(speed)
        for dutyCycle in range(100, -1, -step):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(speed)


def color_test_thread():
    threads = []
    threads.append(threading.Thread(target=color_test, args=(R, 300, 0.02, 5)))
    threads.append(threading.Thread(target=color_test, args=(G, 300, 0.035, 5)))
    threads.append(threading.Thread(target=color_test, args=(B, 300, 0.045, 5)))
    try:
        with Pool(processes=len(threads)) as p:
            # Red
            p.map(color_test)
            # Green
            p.map(color_test()
            # Blue
        # for t in threads:
        #     t.daemon = True
        #     t.start()
        # for t in threads:
        #     t.join()
    except KeyboardInterrupt:
        print("\nPress ^C (control-C) to exit the program.\n")
        GPIO.cleanup()
    finally:
        print("[*] Finished.")
        GPIO.cleanup()



def main():
    global _FINISH
    try:
        initialize_gpio()
        # print("\nPress ^C (control-C) to exit the program.\n")
        color_test_thread()
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()