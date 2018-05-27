import time
import RPi.GPIO as GPIO
#Motor setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.output(27,True)
GPIO.output(22,False)
GPIO.output(23,False)
GPIO.output(24,True)
left=GPIO.PWM(17,100)
right=GPIO.PWM(18,100)
left.start(0)
right.start(0)
print("Motor Setup finished")
time.sleep(1)
# Setup U
GPIO.setmode(GPIO.BCM)
ULTRASONIC_TRIGGER_PINS = [5,6,26]
ULTRASONIC_ECHO_PINS = [11,13,19]
print("Ultrasonic setup finished")
time.sleep(1)
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

def forward(dutyCycle):
    left.ChangeDutyCycle(dutyCycle)
    right.ChangeDutyCycle(dutyCycle)
    GPIO.output(27,True)
    GPIO.output(22,False)
    GPIO.output(23,False)
    GPIO.output(24,True)
def backward(dutyCycle):
    left.ChangeDutyCycle(dutyCycle)
    right.ChangeDutyCycle(dutyCycle)
    GPIO.output(27,False)
    GPIO.output(22,True)
    GPIO.output(23,True)
    GPIO.output(24,False)
    
def setLeft():
    GPIO.output(27,True)
    GPIO.output(22,False)
    GPIO.output(23,True)
    GPIO.output(24,False)
def setRight():
    GPIO.output(27,False)
    GPIO.output(22,True)
    GPIO.output(23,False)
    GPIO.output(24,True)

def zeroMotor():
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)
flag = 0
def slowBreak(startDutyCycle):
    while (startDutyCycle >= 10):
        startDutyCycle = startDutyCycle - 10
        left.ChangeDutyCycle(startDutyCycle)
        right.ChangeDutyCycle(startDutyCycle)
        time.sleep(0.1)

def slowStart(targetDutyCycle):
    currentDutyCycle = 0
    while (currentDutyCycle < targetDutyCycle):
        currentDutyCycle = currentDutyCycle + 10
        left.ChangeDutyCycle(currentDutyCycle)
        right.ChangeDutyCycle(currentDutyCycle)
        time.sleep(0.1)
try:
    while True:
        ultrasonicReading1 = ultrasonic(0)
        ultrasonicReading2 = ultrasonic(1)
        ultrasonicReading3 = ultrasonic(2)
        print "Ultrasonic: %.1f %.1f %.1f " %(ultrasonicReading1,ultrasonicReading2,ultrasonicReading3)
        time.sleep(0.1)
        if(ultrasonicReading1 > 20):
            if(flag):
                slowBreak(80)
                time.sleep(0.5)
                setLeft()
                slowStart(80)
            flag = 0
        else:
            if(not(flag)):
                slowBreak(80)
                time.sleep(0.5)
                setRight()
                slowStart(80)
            flag = 1
except KeyboardInterrupt:
    print("Interrupted! Clean up.")
    left.stop()
    right.stop()
    GPIO.cleanup()
except Exception as e:
    print("Undocumented error. Stopping")
    print(e)
    left.stop()
    right.stop()
    GPIO.cleanup()