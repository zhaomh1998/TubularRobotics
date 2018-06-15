import time, traceback, colorama
import RPi.GPIO as GPIO
colorama.init()

GPIO.setmode(GPIO.BCM)
ULTRASONIC_TRIGGER_PINS = [6,5,26]
ULTRASONIC_ECHO_PINS = [13,11,19]

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
    print("[INFO]\tUltrasonic Started. Distance unit is meters.")
    while True:
        print('Ultrasonic 0'+ str(ultrasonic(0)) + '\t' + 'Ultrasonic 1'+ str(ultrasonic(1)) + '\t' + 'Ultrasonic 2'+ str(ultrasonic(2)))
        time.sleep(0.01) 
except BaseException as e:
    print(colorama.Fore.RED + '[ERROR]\t' + colorama.Style.RESET_ALL + e.message)
    print(colorama.Fore.RED + '[ERROR]\t' + colorama.Style.RESET_ALL + traceback.format_exc())
    GPIO.cleanup()