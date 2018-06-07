# import RPi.GPIO as GPIO
# from time import sleep
# GPIO.setmode(GPIO.BOARD)
#
#
# print("RPi.GPIO Mode BOARD OK")
#
# pin_led_r = 40
# pin_led_g = 38
# pin_led_b = 36
# pin_vcc = 37
#
#
# GPIO.setup(pin_led_r, GPIO.OUT)
# GPIO.setup(pin_led_g, GPIO.OUT)
# GPIO.setup(pin_led_b, GPIO.OUT)
# GPIO.setup(pin_vcc, GPIO.OUT)
#
# GPIO.output(pin_vcc, GPIO.HIGH)
#
# GPIO.output(pin_led_r, GPIO.LOW)
# sleep(1)
# GPIO.output(pin_led_r, GPIO.HIGH)
#
# GPIO.output(pin_led_g, GPIO.LOW)
# sleep(1)
# GPIO.output(pin_led_g, GPIO.HIGH)
#
# GPIO.output(pin_led_b, GPIO.LOW)
# sleep(1)
# GPIO.output(pin_led_b, GPIO.HIGH)

print("Test LED OK")
print("RPi.GPIO Mode BOARD OK")


class LEDs:
    @classmethod
    def setLEDs(cls, color=(0,0,0)):
        pass