import time
import RPi.GPIO as GPIO

class MotorController:
        def __init__(self,LMotorPWNPin,LMotorForwardPin,LMotorBackwardPin,RMotorPWNPin,RMotorForwardPin,RMotorBackwardPin):
            #setup gpios
            GPIO.setup(LMotorPWNPin, GPIO.OUT)
            GPIO.setup(LMotorForwardPin, GPIO.OUT)
            GPIO.setup(LMotorBackwardPin, GPIO.OUT)
            self.__LMotor=GPIO.PWM(LMotorPWNPin,100)
            GPIO.setup(RMotorPWNPin, GPIO.OUT)
            GPIO.setup(RMotorForwardPin, GPIO.OUT)
            GPIO.setup(RMotorBackwardPin, GPIO.OUT)
            self.__RMotor=GPIO.PWM(RMotorPWNPin,100)
            # define pins
            self.__LMotorForwardPin = LMotorForwardPin
            self.__LMotorBackwardPin = LMotorBackwardPin
            self.__RMotorForwardPin = RMotorForwardPin
            self.__RMotorBackwardPin = RMotorBackwardPin
            # init vars
            self.__currentDutyCycle = 0

        def setForward(self):
            GPIO.output(self.__LMotorForwardPin, True)
            GPIO.output(self.__LMotorBackwardPin, False)
            GPIO.output(self.__RMotorForwardPin, True)
            GPIO.output(self.__RMotorBackwardPin, False)

        def setBackward(self):
            GPIO.output(self.__LMotorForwardPin, False)
            GPIO.output(self.__LMotorBackwardPin, True)
            GPIO.output(self.__RMotorForwardPin, False)
            GPIO.output(self.__RMotorBackwardPin, True)

        def setLeft(self):
            GPIO.output(self.__LMotorForwardPin, False)
            GPIO.output(self.__LMotorBackwardPin, True)
            GPIO.output(self.__RMotorForwardPin, True)
            GPIO.output(self.__RMotorBackwardPin, False)

        def setRight(self):
            GPIO.output(self.__LMotorForwardPin, True)
            GPIO.output(self.__LMotorBackwardPin, False)
            GPIO.output(self.__RMotorForwardPin, False)
            GPIO.output(self.__RMotorBackwardPin, True)
        
        def slowBreak(self):
            while (startDutyCycle >= 10):
                startDutyCycle = startDutyCycle - 10
                self.__LMotor.ChangeDutyCycle(startDutyCycle)
                self.__RMotor.ChangeDutyCycle(startDutyCycle)
                time.sleep(0.1)

        def slowStart(self,targetDutyCycle):
            self.__currentDutyCycle = 0
            while (self.__currentDutyCycle < targetDutyCycle):
                self.__currentDutyCycle = self.__currentDutyCycle + 10
                self.__LMotor.ChangeDutyCycle(currentDutyCycle)
                self.__RMotor.ChangeDutyCycle(currentDutyCycle)
                time.sleep(0.1)

        def cleanupMotors(self):
            self.__LMotor.stop()
            self.__RMotor.stop()
            GPIO.cleanup()
            