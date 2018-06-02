import WirelessTool, socket, traceback, logging

TCPServer = WirelessTool.TCPEchoServer(3000,0.1)
Ultrasonic = WirelessTool.TCPClient('127.0.0.1',3001,0.1)
Encoder = WirelessTool.TCPClient('127.0.0.1',3002,0.1)
MainController = WirelessTool.TCPClient('127.0.0.1',3003,3)
while(not TCPServer.connect(5)):
    print("Waiting remote connection")

# Connected
lastFrontUltrasonic = 1
outlierFlag = False
outlierCounter = 0
lastValueBeforeOutlier = 0

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
        # print(UData)
        if(UData != 'Z'):
            UData = UData.split('\t')
            for readings in UData[:-1]:  # Get rid of the last extra \t
                if (readings[1] == '0'):
                    currentUltrasonic = int(readings[2:])
                    if(float(currentUltrasonic) / float(lastFrontUltrasonic) > 1.5 or float(currentUltrasonic) / float(lastFrontUltrasonic) < 0.64):
                        # print float(currentUltrasonic) / float(lastFrontUltrasonic)
                        currentUltrasonic = lastFrontUltrasonic
                        outlierFlag = True
                        outlierCounter = 0
                        lastValueBeforeOutlier = lastFrontUltrasonic
                    else:
                        outlierFlag = False

                    if((not outlierFlag) and (outlierCounter < 5)):
                        outlierCounter += 1
                        currentUltrasonic = lastValueBeforeOutlier
                    print("outlierCount = " + str(outlierCounter) + "\toutlierFlag = " + str(outlierFlag))
                    lastFrontUltrasonic = int(readings[2:])
                    MainController.write('U' + str(currentUltrasonic) + '\t')
                    # print('F_'+str(readings[2:]))
                    # TCPServer.write('U0' + str(readings[:2]))
                # elif (readings[1] == '1'):
                    # print('R_'+str(readings[2:]))
                # elif (readings[1] == '2'):
                    # print('L_'+str(readings[2:]))
        EData = Encoder.read()
        # if(EData != 'Z'):
            
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
    except Exception as e:
        logging.error(traceback.format_exc())
        TCPServer.close()
        Ultrasonic.close()
        MainController.close()