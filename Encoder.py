from RPi import GPIO
from time import sleep
import WirelessTool

R_clk = 10
R_dt = 9
L_clk = 25
L_dt = 8

ECServer = WirelessTool.TCPEchoServer(3002,2,'127.0.0.1')
while(not ECServer.connect(5)):
    print("Encoder Server Waiting Client Connection")

GPIO.setmode(GPIO.BCM)
GPIO.setup(R_clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R_dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(L_clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(L_dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

R_counter = 0
R_clkLastState = GPIO.input(R_clk)
L_counter = 0
L_clkLastState = GPIO.input(L_clk)
try:

        while True:
                R_clkState = GPIO.input(R_clk)
                R_dtState = GPIO.input(R_dt)
                L_clkState = GPIO.input(L_clk)
                L_dtState = GPIO.input(L_dt)
                if R_clkState != R_clkLastState:
                        if R_dtState != R_clkState:
                                R_counter += 1
                        else:
                                R_counter -= 1
                        print R_counter

                if L_clkState != L_clkLastState:
                        if L_dtState != L_clkState:
                                L_counter += 1
                        else:
                                L_counter -= 1
                        print L_counter
                R_clkLastState = R_clkState
                L_clkLastState = L_clkState
                sleep(0.0001)
finally:
        GPIO.cleanup()