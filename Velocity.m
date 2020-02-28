load('TimeArray.mat')
load('mousevals.mat')
load('AIvals.mat')
Human_derivative = diff(double(MousePos))./diff(TimeArray);
AI_derivative = diff(double(AIPos))./diff(TimeArray);
plot(TimeArray(1:end-1), Human_derivative, 'g-', TimeArray(1:end-1), AI_derivative, 'b-', [min(TimeArray) max(TimeArray)], [0 0], 'k-');
xlabel('Time [s]');
ylabel('Velocity [a.u]');
legend('Human Player', 'Virtual Player')
title('Velocity plotted against time');
grid on;