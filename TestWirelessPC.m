% The following is your RPI's IP Address. Make sure it's correct
PI_IP = '172.24.1.1';
pi = tcpclient(PI_IP, 3000);
pi.write(uint8('Hello from MATLAB'))
pause(0.1)
char(pi.read())