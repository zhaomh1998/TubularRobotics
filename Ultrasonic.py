import time,WirelessTool
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
ULTRASONIC_TRIGGER_PINS = [5,6,26]
ULTRASONIC_ECHO_PINS = [11,13,19]


USServer = WirelessTool.TCPEchoServer(3001,2,'127.0.0.1')
while(not USServer.connect(5)):
    print("Ultrasonic Server Waiting Client Connection")

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
        USServer.write('U0'+ str(int(ultrasonic(0))) + '\t')
        time.sleep(0.01)
        USServer.write('U1'+ str(int(ultrasonic(1))) + '\t')
        time.sleep(0.01)
        USServer.write('U2'+ str(int(ultrasonic(2))) + '\t')
        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
    USServer.close()