load('TimeArray.mat')
load('mousevals.mat')
load('AIvals.mat')
%NewMouse = double(MousePos);
%Errors = NewMouse - AIPos;
derivative = diff(ErrorArray)./diff(TimeArray);
plot(TimeArray(1:end-1), derivative, 'b-', [min(TimeArray) max(TimeArray)], [0 0], 'k-');
xlabel('Time [s]');
ylabel('Error function derivative');
title('Error function derivative plotted against time');
grid on;
