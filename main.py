#!/usr/bin/env python
import time
import email_sender
import RPi.GPIO as GPIO
from gpiozero import MotionSensor

pir = MotionSensor(4, queue_len=2, sample_rate=10)

# GPIO Pin
Sw520dPin = 12


# setup function for some setup
def setup_tilt():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Sw520dPin, GPIO.IN)


def destroy():
    GPIO.cleanup()


# Main Function
def main():
    while True:
        pir.wait_for_motion()
        if pir.motion_detected:
            print("Person Detected")
            email_sender.detected(1)
            if (GPIO.input(Sw520dPin)):
                email_sender.detected(2)
            time.sleep(10)


if __name__ == '__main__':
    setup_tilt()
    try:
        main()
    # when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()
