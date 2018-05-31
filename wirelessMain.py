import wirelessTool,struct,MotorController

TCPServer = wirelessTool.TCPEchoServer(3000,2)
car = MotorController.MotorController(17,27,22,18,23,24)
while(not TCPServer.connect(5)):
    print("Waiting remote connection")

# Connected

while(True):
    try:
        data = TCPServer.read()
        if(data == 'a'):
            car.slowBreak()
            car.setForward()
            car.slowStart(30)
        elif(data == 'b'):
            car.slowBreak()
            car.setBackward()
            car.slowStart(30)
        elif(data == 'c'):
            car.slowBreak()
            car.setRight()
            car.slowStart(30)
        elif(data == 'd'):
            car.slowBreak()
            car.setLeft()
            car.slowStart(30)

    except Exception as e:
        print("Error. Stopping")
        print(e)