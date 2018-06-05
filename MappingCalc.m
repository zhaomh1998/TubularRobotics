function [dx,dy,axisAngle] = MappingCalc(rightArcLength,leftArcLength,distanceBetweenTwoWheels,currentAxisTiltAngle)
s1 = rightArcLength;
s2 = leftArcLength;
l = distanceBetweenTwoWheels;
a = currentAxisTiltAngle;
if(s1 == s2)
    s2 = s1 - 0.0000000001; % To avoid zero division error when calculating r
end
%% Calculate position on robot axis
alpha = ((360)*(s2-s1)) / (2*pi*l);
alpha = alpha / 180 * pi;
r = (s1*l)/(s2-s1);

xOnRobotAxis = (r+(1/2)*l)*(1 - cos(alpha));
yOnRobotAxis = (r+(1/2)*l)*(sin(alpha));

%% Convert to standard axis
axisAngle = a + alpha;
mag = (xOnRobotAxis^2 + yOnRobotAxis^2)^(1/2);
if(yOnRobotAxis == 0)
    yOnRobotAxis = 0.0000000001; % To avoid zero division error when calculating beta
end
beta = atan(xOnRobotAxis / yOnRobotAxis);
dx = sin(beta - a)*mag;
dy = cos(beta - a)*mag;
end
