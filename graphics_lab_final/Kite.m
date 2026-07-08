clc; clear; close all

img = zeros(60,60);

p1 = [30 10];
p2 = [10 30];
p3 = [30 50];
p4 = [50 30];

line = @(x1,y1,x2,y2) ...
    arrayfun(@(t) round([x1 + t*(x2-x1), y1 + t*(y2-y1)]), linspace(0,1,200),'UniformOutput',false);

pts = [line(p1(1),p1(2),p2(1),p2(2)), ...
       line(p2(1),p2(2),p3(1),p3(2)), ...
       line(p3(1),p3(2),p4(1),p4(2)), ...
       line(p4(1),p4(2),p1(1),p1(2))];

pts = cell2mat(pts');

for k=1:size(pts,1)
    x = pts(k,1); y = pts(k,2);
    if x>=1 && x<=60 && y>=1 && y<=60
        img(x,y) = 1;
    end
end

t1 = [30 50];
t2 = [27 55];
t3 = [33 55];

tail = [line(t1(1),t1(2),t2(1),t2(2)), ...
        line(t2(1),t2(2),t3(1),t3(2)), ...
        line(t3(1),t3(2),t1(1),t1(2))];

tail = cell2mat(tail');

for k=1:size(tail,1)
    x = tail(k,1); y = tail(k,2);
    if x>=1 && x<=60 && y>=1 && y<=60
        img(x,y) = 1;
    end
end

figure
subplot(1,2,1)
imagesc(img)
axis equal off
title('Before Fill')
colormap(gray)

x = 30; y = 30;
target = img(x,y);
replacement = 0.5;

stack = [x y];

while ~isempty(stack)
    p = stack(end,:);
    stack(end,:) = [];
    i = p(1); j = p(2);

    if i<1 || i>60 || j<1 || j>60
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
colormap(gray)
