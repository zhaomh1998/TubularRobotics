import time, WirelessTool, traceback, colorama
import RPi.GPIO as GPIO
colorama.init()

GPIO.setmode(GPIO.BCM)
ULTRASONIC_TRIGGER_PINS = [6,5,26]
ULTRASONIC_ECHO_PINS = [13,11,19]

USServer = WirelessTool.TCPEchoServer(3001,2,'127.0.0.1')
while(not USServer.connect(5)):
    print("[INFO]\tServer Waiting Connection")

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
    print("[INFO]\tUltrasonic Started")
    while True:
        u0 = int(ultrasonic(0))
        if(u0 > 500):
            continue
        USServer.write('U0'+ str(u0) + '\t')
        # print(u0)
        time.sleep(0.01)
        USServer.write('U1'+ str(int(ultrasonic(1))) + '\t')
        time.sleep(0.01)
        USServer.write('U2'+ str(int(ultrasonic(2))) + '\t')
        time.sleep(0.01) 
except BaseException as e:
    print(colorama.Fore.RED + '[ERROR]\t' + colorama.Style.RESET_ALL + e.message)
    print(colorama.Fore.RED + '[ERROR]\t' + colorama.Style.RESET_ALL + traceback.format_exc())
    GPIO.cleanup()
    USServer.close()