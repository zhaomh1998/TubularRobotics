import wirelessTool,struct

TCPServer = wirelessTool.TCPEchoServer(3000,2)

while(not TCPServer.connect(5)):
    print("Connection failed")

while(True):
    data = TCPServer.read()
    # value, = struct.unpack('H', data[:2])
    print(data)
    TCPServer.write(data)