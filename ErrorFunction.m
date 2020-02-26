load('TimeArray.mat')
load('mousevals.mat')
load('AIvals.mat')
ErrorArray = double(MousePos) -(AIPos);
plot(TimeArray, ErrorArray, 'b-', [min(TimeArray) max(TimeArray)], [0 0], 'k-');
xlabel('Time [s]');
ylabel('Error function, e(t) [a.u]');
%legend('Human Player', 'Virtual Player')

title('Error function plotted against time');
grid on;

