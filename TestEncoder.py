from RPi import GPIO
import time, traceback, colorama
colorama.init()

L_clk = 10
L_dt = 9
R_clk = 25
R_dt = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(R_clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R_dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(L_clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(L_dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

R_counter = 0
R_clkLastState = GPIO.input(R_clk)
L_counter = 0
L_clkLastState = GPIO.input(L_clk)
lastSent = time.time()
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

                if L_clkState != L_clkLastState:
                        if L_dtState != L_clkState:
                                L_counter += 1
                        else:
                                L_counter -= 1
                        # print L_counter
                R_clkLastState = R_clkState
                L_clkLastState = L_clkState
                time.sleep(0.0001)
                timeBefore = time.time()
                if(time.time() - lastSent > 0.1):
                        print('Right Encoder:\t' + str(R_counter) + '\t' + 'Left Encoder:\t' + str(L_counter))
                        lastSent = time.time()
except BaseException as e:
        print(colorama.Fore.RED + '[ERROR]\t' + colorama.Style.RESET_ALL + e.message)
        print(colorama.Fore.RED + '[ERROR]\t' + colorama.Style.RESET_ALL + traceback.format_exc())
        GPIO.cleanup()