import WirelessTool, socket

TCPServer = WirelessTool.TCPEchoServer(3000,0.1)
Ultrasonic = WirelessTool.TCPClient('127.0.0.1',3001,0.1)
# Encoder = WirelessTool.TCPClient('127.0.0.1',3002,0.1)
MainController = WirelessTool.TCPClient('127.0.0.1',3003,3)
while(not TCPServer.connect(5)):
    print("Waiting remote connection")

# Connected

while(True):
    try:
        data = TCPServer.read()
        # print data
        if(data[0] == 'F'):
            print('F')
            print(int(data[1:]))
            TCPServer.write('OK')
            MainController.write(data + '\t')
        elif(data[0] == 'B'):
            print('B')
            print(int(data[1:]))
            TCPServer.write('OK')
            MainController.write(data + '\t')
        elif(data[0] == 'L'):
            print('L')
            print(int(data[1:]))
            TCPServer.write('OK')
            MainController.write(data + '\t')
        elif(data[0] == 'R'):
            print('R')
            print(int(data[1:]))
            TCPServer.write('OK')
            MainController.write(data + '\t')
        elif(data[0] == 'S'):
            print('S')
            TCPServer.write('OK')
            MainController.write(data + '\t')
        UData = Ultrasonic.read()
        print(UData)
        if(UData != 'Z'):
            UData = UData.split('\t')
            for readings in UData[:-1]:  #Get rid of the last extra \t
                if (readings[1] == '0'):
                    MainController.write('U' + str(readings[2:]) + '\t')
                    print('F_'+str(readings[2:]))
                    # TCPServer.write('U0' + str(readings[:2]))
                elif (readings[1] == '1'):
                    print('R_'+str(readings[2:]))
                elif (readings[1] == '2'):
                    print('L_'+str(readings[2:]))
    # except Exception as e:
    #     print("Error. Stopping")
    #     print(e)
    #     TCPServer.close()
    #     Ultrasonic.close()
        # Encoder.close()
    except KeyboardInterrupt:
        TCPServer.close()
        Ultrasonic.close()
        MainController.close()
    except socket.error:
        TCPServer.close()
        Ultrasonic.close()
        MainController.close()