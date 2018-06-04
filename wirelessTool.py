import socket, colorama

class TCPEchoServer:
    def __init__(self,port,receiveTimeout,listeningIPAddress='0.0.0.0'):
        self.__recvTimeout = receiveTimeout
        self.__serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__serverSock.bind((listeningIPAddress, port))
        self.__serverSock.listen(1)
        # print("Server started. Listening connections")
    
    def connect(self,timeout=5):
        try:
            self.__serverSock.settimeout(timeout)
            self.__clientsocket,self.__addr = self.__serverSock.accept()
            print("Connection from %s" % str(self.__addr))
            self.__clientsocket.settimeout(self.__recvTimeout)
            return True
        except socket.timeout:
            # print("Timeout awaiting connection")
            return False

    def getClientAddr(self):
        return self.__addr

    def setRecvTimeout(self,receiveTimeout):
        self.__recvTimeout = receiveTimeout
        self.__clientsocket.settimeout(self.__recvTimeout)
        return True
    def read(self):
        try:
            return self.__clientsocket.recv(1024)
        except socket.timeout:
            # print("Timeout awaiting message")
            return 'Z' # timeout awaiting message
            
    def write(self,data):
        self.__clientsocket.send(data)
        return True
    def close(self):
        # self.__clientsocket.shutdown(1)
        print(colorama.Fore.GREEN + '[CLEANUP]\t' + colorama.Style.RESET_ALL + 'Closing Server')
        self.__clientsocket.close()
        self.__serverSock.close()
        return True

class TCPClient:
    def __init__(self,addr,port,timeout=0.1,bufferSize=1024):
        self.__TCP_IP = addr
        self.__TCP_PORT = port
        self.__BUFFER_SIZE = bufferSize
        self.__TIME_OUT = timeout
        self.__clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__clientSock.connect((self.__TCP_IP, self.__TCP_PORT))
        self.__clientSock.settimeout(self.__TIME_OUT)
    def write(self,message):
        self.__clientSock.send(message)

    def read(self):
        try:
            return self.__clientSock.recv(self.__BUFFER_SIZE)
        except socket.timeout:
            # print("Timeout awaiting message")
            return 'Z' # timeout awaiting message
    def close(self):
        print(colorama.Fore.GREEN + '[CLEANUP]\t' + colorama.Style.RESET_ALL + 'Closing client socket')
        self.__clientSock.close()
        return True