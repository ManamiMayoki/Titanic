clc; clear; close all;
X1 = 2; Y1 = 3;
X2 = 12; Y2 = 8;
DX = X2 - X1;
DY = Y2 - Y1;
STEPS = max(abs(DX), abs(DY));
X_INC = DX / STEPS;
Y_INC = DY / STEPS;
X = X1;
Y = Y1;
figure;
hold on;
grid on;
axis equal;
title('DDA Algorithm');
xlabel('X-axis'); ylabel('Y-axis');
for I = 1:STEPS+1
    plot(round(X), round(Y), 'ks', 'MarkerSize', 8, 'MarkerFaceColor', 'k');
    X = X + X_INC;
    Y = Y + Y_INC;
end
plot([X1 X2], [Y1 Y2], 'r--');
