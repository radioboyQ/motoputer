import time

import pigpio

pi = pigpio.pi()

print("50% power, blue.")
pi.set_PWM_dutycycle(20, 255*0.50)

time.sleep(3)

print("Blue off.")
pi.write(20, 1)
# pi.set_PWM_dutycycle(20, 0)