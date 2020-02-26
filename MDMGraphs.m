load('TimeArray.mat')
load('mousevals.mat')
load('AIvals.mat')
plot(TimeArray, MousePos, 'g-', TimeArray, AIPos, 'b-', [min(TimeArray) max(TimeArray)], [0 0], 'k-');
xlabel('Time [s]');
ylabel('Position [a.u]');
legend('Human Player', 'Virtual Player')

title('Position plotted against time');
grid on;


