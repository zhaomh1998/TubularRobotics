import WirelessTool, MotorController, traceback, colorama, time
colorama.init()

command = WirelessTool.TCPEchoServer(3003,2)
car = MotorController.MotorController(18,23,24,17,27,22)
while(not command.connect(5)):
    print("Waiting connection from commander")

# Connected
isManual = True
USReading = 50
currentSpeed = 0.0
isGoingForward = True
startUp = False
while(True):
    try:
        received = command.read()
        if(received != 'z'):
            received = received.split('\t')
            # print received
            for data in received[:-1]:
                if(data[0] == 'F' and USReading > 20):
                    isGoingForward = True
                    isManual = True
                    car.slowBreak()
                    car.setForward()
                    currentSpeed = int(data[1:])
                    car.slowStart(currentSpeed)
                    # car.fastStart(currentSpeed)
                elif(data[0] == 'B'):
                    isManual = True
                    car.slowBreak()
                    car.setBackward()
                    currentSpeed = int(data[1:])
                    car.slowStart(currentSpeed)
                elif(data[0] == 'R'):
                    isManual = True
                    car.slowBreak()
                    car.setRight()
                    currentSpeed = int(data[1:])
                    car.slowStart(currentSpeed)
                elif(data[0] == 'L'):
                    isManual = True
                    car.slowBreak()
                    car.setLeft()
                    currentSpeed = int(data[1:])
                    car.slowStart(currentSpeed)
                elif(data[0] == 'S'):
                    isManual = True
                    car.slowBreak()
                elif(data[0] == 'A'):
                    if(int(data[1:]) == 1):
                        isManual = False
                        car.setForward()
                    else:
                        isManual = True
                elif(data[0] == 'U'):
                    USReading = float(data[1:])
                    # print (USReading)
                    if((USReading < (40 + currentSpeed)) and isGoingForward):
                        print('\t' + str(USReading))
                        car.slowBreak()
                        isGoingForward = False
                        print(colorama.Fore.LIGHTBLUE_EX + '[DEBUG]\t' + colorama.Style.RESET_ALL + 'Slow break finished')
                
            if(not isManual):
                distanceForward = USReading - 80
                print(colorama.Fore.YELLOW + '[AUTO]\t' + colorama.Style.RESET_ALL + str(distanceForward))
                if(distanceForward <= 0):
                    car.slowBreak()
                    time.sleep(0.5)
                    if(startUp):
                        print(colorama.Fore.GREEN + '[CONTROL]\t' + colorama.Style.RESET_ALL + 'Going backward')
                        car.setBackward()
                        car.fastStart(0)
                        time.sleep(1)
                        car.setForward()
                        startUp = False
                    print(colorama.Fore.GREEN + '[CONTROL]\t' + colorama.Style.RESET_ALL + 'Start turning')
                    car.setRight()
                    # car.fastStart(50)
                    car.slowStart(55)
                    car.slowBreak()
                    print(colorama.Fore.GREEN + '[CONTROL]\t' + colorama.Style.RESET_ALL + 'Turning Finished')
                    car.setForward()
                elif(distanceForward < 50):
                    startUp = True
                    car.changeSpeed(25)
                elif(distanceForward < 100):
                    startUp = True
                    car.changeSpeed(28)
                else:
                    startUp = True
                    car.changeSpeed(30)


    except BaseException as e:
        print(colorama.Fore.RED + '[ERROR]\t' + colorama.Style.RESET_ALL + e.message)
        print(colorama.Fore.RED + '[ERROR]\t' + colorama.Style.RESET_ALL + traceback.format_exc())
        command.close()
        car.close()
        break