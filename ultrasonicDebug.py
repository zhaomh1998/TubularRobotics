import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
ULTRASONIC_TRIGGER_PINS = [11,14]
ULTRASONIC_ECHO_PINS = [13,15]

# Setup GPIO Pins for Ultrasonic
for gpioPin in ULTRASONIC_TRIGGER_PINS:
    GPIO.setup(gpioPin,GPIO.OUT)
    time.sleep(0.1)
    GPIO.output(gpioPin,False)
for gpioPin in ULTRASONIC_ECHO_PINS:
    GPIO.setup(gpioPin,GPIO.IN)


def ultrasonic(ultrasonicIndex):
    time.sleep(0.01)
    GPIO.output(ULTRASONIC_TRIGGER_PINS[ultrasonicIndex], True)
    time.sleep(0.00001)
    GPIO.output(ULTRASONIC_TRIGGER_PINS[ultrasonicIndex], False)
    timeSent = time.time()
    start = timeSent
    while GPIO.input(ULTRASONIC_ECHO_PINS[ultrasonicIndex])==0:
        start = time.time()
        if(start - timeSent) > 0.05:
            return 2200  #Timeout
    echoTime = time.time()
    while GPIO.input(ULTRASONIC_ECHO_PINS[ultrasonicIndex])==1:
        echoTime = time.time()
    return (echoTime-start) * 34300/2


try:
    while True:
        print "Ultrasonic: %.1f %.1f" %(ultrasonic(0), ultrasonic(1))
        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()