function varargout = TR(varargin)
% TR MATLAB code for TR.fig
%      TR, by itself, creates a new TR or raises the existing
%      singleton*.
%
%      H = TR returns the handle to a new TR or the handle to
%      the existing singleton*.
%
%      TR('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in TR.M with the given input arguments.
%
%      TR('Property','Value',...) creates a new TR or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before TR_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to TR_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help TR

% Last Modified by GUIDE v2.5 03-Jun-2018 18:01:09

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @TR_OpeningFcn, ...
                   'gui_OutputFcn',  @TR_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before TR is made visible.
function TR_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to TR (see VARARGIN)

% Choose default command line output for TR
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes TR wait for user response (see UIRESUME)
% uiwait(handles.figure1);
%% Initialize connection
global pi
PI_IP = '172.24.1.1';
% PI_IP = '127.0.0.1';
% PI_IP = '192.168.137.106'
pi = tcpclient(PI_IP, 3000);

%% Initialize vars
global pwm
pwm = 0;


% --- Outputs from this function are returned to the command line.
function varargout = TR_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in PB_F.
function PB_F_Callback(hObject, eventdata, handles)
global pi pwm
set(handles.Status1,'String','Sending command..')
set(handles.Status2,'String','')
set(handles.isAuto,'Value',0)
pi.write(uint8(['F' int2str(pwm)]))
pause(0.1)
% recv = char(pi.read());
% set(handles.Status2,'String',recv)

% --- Executes on button press in PB_R.
function PB_R_Callback(hObject, eventdata, handles)
global pi pwm
set(handles.Status1,'String','Sending command..')
set(handles.Status2,'String','')
set(handles.isAuto,'Value',0)
pi.write(uint8(['R' int2str(pwm)]))
pause(0.1)
% recv = char(pi.read());
% set(handles.Status2,'String',recv)

% --- Executes on button press in PB_L.
function PB_L_Callback(hObject, eventdata, handles)
global pi pwm
set(handles.Status1,'String','Sending command..')
set(handles.Status2,'String','')
set(handles.isAuto,'Value',0)
pi.write(uint8(['L' int2str(pwm)]))
pause(0.1)
% recv = char(pi.read());
% set(handles.Status2,'String',recv)

% --- Executes on button press in PB_B.
function PB_B_Callback(hObject, eventdata, handles)
global pi pwm
set(handles.Status1,'String','Sending command..')
set(handles.Status2,'String','')
set(handles.isAuto,'Value',0)
pi.write(uint8(['B' int2str(pwm)]))
pause(0.1)
% recv = char(pi.read());
% set(handles.Status2,'String',recv)

% --- Executes on button press in PB_S.
function PB_S_Callback(hObject, eventdata, handles)
global pi
set(handles.Status1,'String','Sending command..')
set(handles.Status2,'String','')
set(handles.isAuto,'Value',0)
pi.write(uint8('S'))
pause(0.1)
% recv = char(pi.read());
% set(handles.Status2,'String',recv)


% --- Executes on slider movement.
function Speed_Slider_Callback(hObject, eventdata, handles)
% hObject    handle to Speed_Slider (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global pwm
pwm = floor(get(hObject,'Value'));
set(handles.Speed_Indicator,'String',pwm)


% --- Executes during object creation, after setting all properties.
function Speed_Slider_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Speed_Slider (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on button press in isAuto.
function isAuto_Callback(hObject, eventdata, handles)
% hObject    handle to isAuto (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of isAuto
global pi
if(get(hObject,'Value'))
    pi.write(uint8(['A' int2str(1)]))
else
    pi.write(uint8(['A' int2str(0)]))
end


% --- Executes on button press in PB_StartPlot.
function PB_StartPlot_Callback(hObject, eventdata, handles)
% hObject    handle to PB_StartPlot (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global pi
count = 1; u0count = 1; u1count = 1; u2count = 1;
u0t=[];u0=[];u1t=[];u1=[];u2t=[];u2=[];
u0locx=zeros(1,2);u0locy=zeros(1,2);
u1locx=zeros(1,2);u1locy=zeros(1,2);
u2locx=zeros(1,2);u2locy=zeros(1,2);
u0LastEncoder1=0;u0LastEncoder2=0;u0Angle=0;
u1LastEncoder1=0;u1LastEncoder2=0;u1Angle=0;
u2LastEncoder1=0;u2LastEncoder2=0;u2Angle=0;
pi.read(); % Flush buffer
while(1)
    data = char(pi.read());
    if(~isempty(data))
        a(count) = string(data);
        if(data(1) == 'U')
            %% Parse Incoming String
            dataStr = string(data);
            ultrasonicIndexLocationsInPacket = strfind(dataStr,'U') + 1;
            dataStr = extractBetween(dataStr, "[", "]");
            for packetIndex = 1:(length(dataStr)/4) % Handles multiple packets
            dataVal = dataStr(1+(packetIndex - 1)*4);
            dataVal = regexprep(dataVal,'[\n\r]+',' ');
            dataVal = str2num(char(dataVal));
            dataTime = dataStr(2+(packetIndex - 1)*4);
            dataTime = regexprep(dataTime,'[\n\r]+',' ');
            dataTime = str2num(char(dataTime));
            set(handles.Status2,'String',dataTime(end))
            if(data(ultrasonicIndexLocationsInPacket(packetIndex)) == '0')
                u0t = [u0t dataTime];
                u0 = [u0 dataVal];
                        %% Parse Encoder Data
                        u0DataEncoder1 = dataStr(3+(packetIndex - 1)*4);
                        u0DataEncoder1 = regexprep(u0DataEncoder1,'[\n\r]+',' ');
                        u0DataEncoder1 = str2num(char(u0DataEncoder1));
                        u0DataEncoder2 = dataStr(4+(packetIndex - 1)*4);
                        u0DataEncoder2 = regexprep(u0DataEncoder2,'[\n\r]+',' ');
                        u0DataEncoder2 = str2num(char(u0DataEncoder2));
                        %% Calculate Encoder difference (s1,s2)
                        u0DiffDataEncoder1 = [(u0DataEncoder1(1) - u0LastEncoder1) diff(u0DataEncoder1)];
                        u0DiffDataEncoder2 = [(u0DataEncoder2(1) - u0LastEncoder2) diff(u0DataEncoder2)];
                        u0LastEncoder1 = u0DataEncoder1(end);
                        u0LastEncoder2 = u0DataEncoder2(end);
                        %% Calculate Positions
                        for i = 1:10
                            ii = (u0count-1)*10 + i;
                            [posx, posy, u0Angle] = MappingCalc(u0DiffDataEncoder1(i),u0DiffDataEncoder2(i),24,u0Angle);
                            u0locx(ii) = u0locx(max(1,ii-1)) + posx;
                            u0locy(ii) = u0locy(max(1,ii-1)) + posy;
                            sinAlpha = sin(u0Angle); cosAlpha = cos(u0Angle);
                            u0xfdata(ii) = u0locx(ii) + u0(ii)*sinAlpha;
                            u0yfdata(ii) = u0locy(ii) + u0(ii)*cosAlpha;
%                             fprintf('#%d\t%.2f\t%.2f\t\t%.2f\t%.2f\n',ii,u0locx(ii),u0locy(ii),u0xfdata(ii),u0yfdata(ii))
                        end 
                        hold on
                        plot(handles.ax1,u0locx,u0locy,'k.')
                        plot(handles.ax1,u0xfdata,u0yfdata,'r.') % Data received by front ultrasonic
                        xlim([-500 500])
                        ylim([-500 500])
                u0count = u0count + 1;
            elseif(data(ultrasonicIndexLocationsInPacket(packetIndex)) == '1')
                u1t = [u1t dataTime];
                u1 = [u1 dataVal];
                        %% Parse Encoder Data
                        u1DataEncoder1 = dataStr(3+(packetIndex - 1)*4);
                        u1DataEncoder1 = regexprep(u1DataEncoder1,'[\n\r]+',' ');
                        u1DataEncoder1 = str2num(char(u1DataEncoder1));
                        u1DataEncoder2 = dataStr(4+(packetIndex - 1)*4);
                        u1DataEncoder2 = regexprep(u1DataEncoder2,'[\n\r]+',' ');
                        u1DataEncoder2 = str2num(char(u1DataEncoder2));
                        %% Calculate Encoder difference (s1,s2)
                        u1DiffDataEncoder1 = [(u1DataEncoder1(1) - u1LastEncoder1) diff(u1DataEncoder1)];
                        u1DiffDataEncoder2 = [(u1DataEncoder2(1) - u1LastEncoder2) diff(u1DataEncoder2)];
                        u1LastEncoder1 = u1DataEncoder1(end);
                        u1LastEncoder2 = u1DataEncoder2(end);
                        %% Calculate Positions
                        for i = 1:10
                            ii = (u1count-1)*10 + i;
                            [posx, posy, u1Angle] = MappingCalc(u1DiffDataEncoder1(i),u1DiffDataEncoder2(i),24,u1Angle);
                            u1locx(ii) = u1locx(max(1,ii-1)) + posx;
                            u1locy(ii) = u1locy(max(1,ii-1)) + posy;
                            sinAlpha = sin(u1Angle); cosAlpha = cos(u1Angle);
                            u1xrdata(ii) = u1locx(ii) + (u1(ii) + 0.5*24)*cosAlpha;
                            u1yrdata(ii) = u1locy(ii) - (u1(ii) + 0.5*24)*sinAlpha;
%                             fprintf('#%d\t%.2f\t%.2f\t\t%.2f\t%.2f\n',ii,u1locx(ii),u1locy(ii),u1xrdata(ii),u1yrdata(ii))
                        end 
                        hold on
                        plot(handles.ax1,u1locx,u1locy,'k.')
                        plot(handles.ax1,u1xrdata,u1yrdata,'g.') % Data received by right ultrasonic
                        xlim([-500 500])
                        ylim([-500 500])
                u1count = u1count + 1;
            elseif(data(ultrasonicIndexLocationsInPacket(packetIndex)) == '2')
                u2t = [u2t dataTime];
                u2 = [u2 dataVal];
                        %% Parse Encoder Data
                        u2DataEncoder1 = dataStr(3+(packetIndex - 1)*4);
                        u2DataEncoder1 = regexprep(u2DataEncoder1,'[\n\r]+',' ');
                        u2DataEncoder1 = str2num(char(u2DataEncoder1));
                        u2DataEncoder2 = dataStr(4+(packetIndex - 1)*4);
                        u2DataEncoder2 = regexprep(u2DataEncoder2,'[\n\r]+',' ');
                        u2DataEncoder2 = str2num(char(u2DataEncoder2));
                        %% Calculate Encoder difference (s1,s2)
                        u2DiffDataEncoder1 = [(u2DataEncoder1(1) - u2LastEncoder1) diff(u2DataEncoder1)];
                        u2DiffDataEncoder2 = [(u2DataEncoder2(1) - u2LastEncoder2) diff(u2DataEncoder2)];
                        u2LastEncoder1 = u2DataEncoder1(end);
                        u2LastEncoder2 = u2DataEncoder2(end);
                        %% Calculate Positions
                        for i = 1:10
                            ii = (u2count-1)*10 + i;
                            [posx, posy, u2Angle] = MappingCalc(u2DiffDataEncoder1(i),u2DiffDataEncoder2(i),24,u2Angle);
                            u2locx(ii) = u2locx(max(1,ii-1)) + posx;
                            u2locy(ii) = u2locy(max(1,ii-1)) + posy;
                            sinAlpha = sin(u2Angle); cosAlpha = cos(u2Angle);
                            u2xldata(ii) = u2locx(ii) - (u2(ii) + 0.5*24)*cosAlpha;
                            u2yldata(ii) = u2locy(ii) + (u2(ii) + 0.5*24)*sinAlpha;
%                             fprintf('#%d\t%.2f\t%.2f\t\t%.2f\t%.2f\n',ii,u2locx(ii),u2locy(ii),u2xldata(ii),u2yldata(ii))
                        end 
                        hold on
                        plot(handles.ax1,u2locx,u2locy,'k.')
                        plot(handles.ax1,u2xldata,u2yldata,'b.') % Data received by left ultrasonic
                        xlim([-500 500])
                        ylim([-500 500])
                u2count = u2count + 1;
            end
            count = count + 1;
            % TODO: Automatically saves data each loop
            end
        end
        end
    pause(0.1)
end
