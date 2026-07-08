clc; clear; close all

img = zeros(50,50);
img(10:40,10:40) = 1;
img(20:30,20:30) = 0;

figure
subplot(1,2,1)
imagesc(img)
axis equal off
title('Before Fill')

x = 25; y = 25;
target = img(x,y);
replacement = 2;

stack = [x y];

while ~isempty(stack)
    p = stack(end,:);
    stack(end,:) = [];
    i = p(1); j = p(2);

    if i<1 || i>50 || j<1 || j>50
        continue
    end

    if img(i,j) ~= target
        continue
    end

    img(i,j) = replacement;

    stack = [stack;
             i+1 j;
             i-1 j;
             i j+1;
             i j-1];
end

subplot(1,2,2)
imagesc(img)
axis equal off
title('After Fill')
colormap(jet)
