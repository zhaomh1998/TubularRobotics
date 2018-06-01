import WirelessTool, MotorController

command = WirelessTool.TCPEchoServer(3003,2)
car = MotorController.MotorController(18,23,24,17,27,22)
while(not command.connect(5)):
    print("Waiting connection from commander")

# Connected
isManual = True
USReading = 50
flag = 1

while(True):
    try:
        received = command.read()
        if(received != 'z'):
            received = received.split('\t')
            # print received
            for data in received[:-1]:
                print data
                if(data[0] == 'F' and USReading > 20):
                    isManual = True
                    car.slowBreak()
                    car.setForward()
                    car.slowStart(int(data[1:]))
                    print('F')
                    command.write('OK')
                elif(data[0] == 'B'):
                    isManual = True
                    car.slowBreak()
                    car.setBackward()
                    car.slowStart(int(data[1:]))
                    print('B')
                    command.write('OK')
                elif(data[0] == 'R'):
                    isManual = True
                    car.slowBreak()
                    car.setRight()
                    car.slowStart(int(data[1:]))
                    print('L')
                    command.write('OK')
                elif(data[0] == 'L'):
                    isManual = True
                    car.slowBreak()
                    car.setLeft()
                    car.slowStart(int(data[1:]))
                    print('R')
                    command.write('OK')
                elif(data[0] == 'S'):
                    isManual = True
                    car.slowBreak()
                    print('S')
                    command.write('OK')
                elif(data[0] == 'U'):
                    USReading = int(data[1:])
                    if(USReading < 20):
                        car.slowBreak()

                if(not isManual):
                    if(USReading > 20):
                        car.setForward()
                        if(flag):
                            car.slowStart(30)
                            flag = 0
                    else:
                        if(not flag): # First time 
                            car.slowBreak()


    except Exception as e:
        print("Error. Stopping")
        print(e)
        command.close()
        car.close()