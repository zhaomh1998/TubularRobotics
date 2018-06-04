x = []
y = []
% for i = (0.1:0.01:10)
%     [a,b] = MappingCalc(0.05,i,0.2);
%     x = [x a];
%     y = [y b];
% end
for i = (0:0.1:10)
    [a,b] = MappingCalc(i,-i,0.2);
    x = [x a];
    y = [y b];
end
plot(x,y,'o')
% comet(x,y)