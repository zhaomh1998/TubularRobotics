import WirelessTool, socket, traceback, colorama
colorama.init()

TCPServer = WirelessTool.TCPEchoServer(3000,0.1)

while(not TCPServer.connect(10)):
    print("[INFO]\tWaiting User Connection")

try:
    while(True):
        userCommand = TCPServer.read()
        if(userCommand != 'Z'): #From WirelessTool, a return 'Z' means no response
            print('Received from client: ' + userCommand + '\t Sending Response ...')
            TCPServer.write('Greetings from RPI! I got your message: ' + userCommand)
            print('Response sent')
            break

except BaseException as e:
    print(colorama.Fore.RED + '[ERROR]\t' + colorama.Style.RESET_ALL + traceback.format_exc())

finally:
    TCPServer.close()