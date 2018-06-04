import WirelessTool, socket, traceback, colorama, time
import numpy as np
colorama.init()

TCPServer = WirelessTool.TCPEchoServer(3000,0.1)
Ultrasonic = WirelessTool.TCPClient('127.0.0.1',3001,0.1)
Encoder = WirelessTool.TCPClient('127.0.0.1',3002,0.1)
MainController = WirelessTool.TCPClient('127.0.0.1',3003,3)
while(not TCPServer.connect(10)):
    print("[INFO]\tWaiting User Connection")
# TODO: If user not connected, go to auto mode
# Connected
U0Readings = np.zeros(9)
U1Readings = np.zeros(9)
U2Readings = np.zeros(9)
U0Buffer = np.zeros((10,2))
U1Buffer = np.zeros((10,2))
U2Buffer = np.zeros((10,2))
E0Buffer = np.zeros((10,2))
E1Buffer = np.zeros((10,2))
U0Count = 0
U1Count = 0
U2Count = 0
E0Count = 0
E1Count = 0


def decodeCommand(rawData):
    recvLength = len(rawData)
    if(recvLength < 1):
        return [('Z', 0, '0')]
    elif(recvLength == 1):
        if(rawData == 'S'):
            return [('S', 0, '0')]
        else:
            return [('Z', 0, '0')]
    else:
        rawData = rawData.split('\t')
        indexCounter = 0
        commandList = []
        for element in rawData:
            if(len(element) == 0): # Handles the extra '' sometime when spliting
                continue
            elif(element[0] == 'U' or element[0] == 'E'):
                commandList.append((element[0], int(element[1]), element[2:]))
            elif(element[0] == 'F' or element[0] == 'B' or element[0] == 'L' or element[0] == 'R' or element[0] == 'A'):
                commandList.append((element[0], 0, element[1:]))
            else:
                print('[ERROR]\tUnexpected command received:->' + element + '<-')
        return commandList

def prepareData(command,data):
    dataTime = time.time() - initTime
    if (command == 'U0'):
        global U0Count
        U0Buffer[U0Count][0] = float(data)
        U0Buffer[U0Count][1] = dataTime
        if(U0Count == 9): # Buffer full, send
            U0Count = -1
            sendArray('U0', U0Buffer)
        U0Count += 1
    elif (command == 'U1'):
        global U1Count
        U1Buffer[U1Count][0] = float(data)
        U1Buffer[U1Count][1] = dataTime
        if(U1Count == 9): # Buffer full, send
            U1Count = -1
            sendArray('U1', U1Buffer)
        U1Count += 1
    elif (command == 'U2'):
        global U2Count
        U2Buffer[U2Count][0] = float(data)
        U2Buffer[U2Count][1] = dataTime
        if(U2Count == 9): # Buffer full, send
            U2Count = -1
            sendArray('U2', U2Buffer)
        U2Count += 1
    elif (command == 'E0'):
        global E0Count
        E0Buffer[E0Count][0] = float(data)
        E0Buffer[E0Count][1] = dataTime
        if(E0Count == 9): # Buffer full, send
            E0Count = -1
            sendArray('E0', E0Buffer)
        E0Count += 1
    elif (command == 'E1'):
        global E1Count
        E1Buffer[E1Count][0] = float(data)
        E1Buffer[E1Count][1] = dataTime
        if(E1Count == 9): # Buffer full, send
            E1Count = -1
            sendArray('E0', E1Buffer)
        E1Count += 1

def sendArray(dataTypeName, dataArr):
    dataStream = dataTypeName + '\t' + np.array_str(dataArr[:,0]) + '\t' + np.array_str(dataArr[:,1])
    TCPServer.write(dataStream)

initTime = time.time()
Ultrasonic.read() # Clear ultrasonic buffer
while(True):
    try:
        userCommand = TCPServer.read()
        for command,index,data in decodeCommand(userCommand):
            if(command == 'Z'):
                pass
            elif(command == 'F'):
                print(colorama.Fore.YELLOW + '[MANUAL]\t' + colorama.Style.RESET_ALL + '\tForward' + data)
                # TCPServer.write('OK')
                MainController.write(command + data + '\t')
            elif(command == 'B'):
                print(colorama.Fore.YELLOW + '[MANUAL]\t' + colorama.Style.RESET_ALL + '\tBackward ' + data)
                # TCPServer.write('OK')
                MainController.write(command + data + '\t')
            elif(command == 'L'):
                print(colorama.Fore.YELLOW + '[MANUAL]\t' + colorama.Style.RESET_ALL + '\tLeft ' + data)
                # TCPServer.write('OK')
                MainController.write(command + data + '\t')
            elif(command == 'R'):
                print(colorama.Fore.YELLOW + '[MANUAL]\t' + colorama.Style.RESET_ALL + '\tRight ' + data)
                # TCPServer.write('OK')
                MainController.write(command + data + '\t')
            elif(command == 'S'):
                print(colorama.Fore.YELLOW + '[MANUAL]\t' + colorama.Style.RESET_ALL + '\tStop')
                # TCPServer.write('OK')
                MainController.write(command + data + '\t')
            elif(command == 'A'):
                print(colorama.Fore.YELLOW + '[MANUAL]\t' + colorama.Style.RESET_ALL + '\tAutomatic Mode switch: ' + data)
                # TCPServer.write('OK')
                MainController.write(command + data + '\t')

        UData = Ultrasonic.read()
        for command,index,data in decodeCommand(UData):
            if(command != 'Z'):
                # prepareData(command + str(index), data)
                if (index == 0):
                    U0Readings = np.append(np.delete(U0Readings,0),int(data))
                    # print(np.median(U0Readings))
                    prepareData('U0', np.median(U0Readings))
                    MainController.write('U' + str(np.median(U0Readings)) + '\t')
                elif (index == 1):
                    U1Readings = np.append(np.delete(U1Readings,0),int(data))
                    # print('\t' + str(np.median(U1Readings)))
                    prepareData('U1', np.median(U1Readings))
                elif (index == 2):
                    U2Readings = np.append(np.delete(U2Readings,0),int(data))
                    # print('\t\t' + str(np.median(U2Readings)))
                    prepareData('U2', np.median(U2Readings))

        EData = Encoder.read()
        for command,index,data in decodeCommand(EData):
            if(command != 'Z'):
                prepareData(command + str(index), data)

    except BaseException as e:
        print(colorama.Fore.RED + '[ERROR]\t' + colorama.Style.RESET_ALL + e.message)
        print(colorama.Fore.RED + '[ERROR]\t' + colorama.Style.RESET_ALL + traceback.format_exc())
        TCPServer.close()
        Ultrasonic.close()
        # Encoder.close()
        MainController.close()
        break