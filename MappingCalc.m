function [x,y] = MappingCalc(s1,s2,l)
% s1 = 1;
% s2 = 2;
% l = 0.2;
alpha = ((360)*(s2-s1)) / (2*pi*l);
alpha = alpha / 180 * pi;
r = (s1*l)/(s2-s1);

x = (r+(1/2)*l)*(1 - cos(alpha));
y = (r+(1/2)*l)*(sin(alpha));

end
