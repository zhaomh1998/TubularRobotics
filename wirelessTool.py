import socket

class TCPEchoServer:
    def __init__(self,port,receiveTimeout):
        self.__recvTimeout = receiveTimeout
        self.__serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__serverSock.bind(('0.0.0.0', port))
        self.__serverSock.listen(1)
        print("Server started. Listening connections")
    
    def connect(self,timeout):
        try:
            self.__serverSock.settimeout(timeout)
            self.__clientsocket,self.__addr = self.__serverSock.accept()
            print("Connection from %s" % str(self.__addr))
            return True
        except socket.timeout:
            print("Timeout awaiting connection")
            return False

    def getClientAddr(self):
        return self.__addr

    def setRecvTimeout(self,receiveTimeout):
        self.__recvTimeout = receiveTimeout
        return True
    def read(self):
        try:
            self.__clientsocket.settimeout(self.__recvTimeout)
            return self.__clientsocket.recv(1024)
        except socket.timeout:
            print("Timeout awaiting connection")
            return 'z' # timeout awaiting connection
            
    def write(self,data):
        self.__clientsocket.send(data)
        return True
    def closeConnection(self):
        self.__clientsocket.shutdown(1)
        self.__clientsocket.close()
        return True