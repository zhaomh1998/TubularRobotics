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

% Last Modified by GUIDE v2.5 31-May-2018 14:47:04

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
pi = tcpclient(PI_IP, 3000);

%% Initialize vard
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
pi.write(uint8(['F' int2str(pwm)]))
pause(0.1)
recv = char(pi.read());
set(handles.Status2,'String',recv)

% --- Executes on button press in PB_R.
function PB_R_Callback(hObject, eventdata, handles)
global pi pwm
set(handles.Status1,'String','Sending command..')
set(handles.Status2,'String','')
pi.write(uint8(['R' int2str(pwm)]))
pause(0.1)
recv = char(pi.read());
set(handles.Status2,'String',recv)

% --- Executes on button press in PB_L.
function PB_L_Callback(hObject, eventdata, handles)
global pi pwm
set(handles.Status1,'String','Sending command..')
set(handles.Status2,'String','')
pi.write(uint8(['L' int2str(pwm)]))
pause(0.1)
recv = char(pi.read());
set(handles.Status2,'String',recv)

% --- Executes on button press in PB_B.
function PB_B_Callback(hObject, eventdata, handles)
global pi pwm
set(handles.Status1,'String','Sending command..')
set(handles.Status2,'String','')
pi.write(uint8(['B' int2str(pwm)]))
pause(0.1)
recv = char(pi.read());
set(handles.Status2,'String',recv)

% --- Executes on button press in PB_S.
function PB_S_Callback(hObject, eventdata, handles)
global pi
set(handles.Status1,'String','Sending command..')
set(handles.Status2,'String','')
pi.write(uint8('S'))
pause(0.1)
recv = char(pi.read());
set(handles.Status2,'String',recv)


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
