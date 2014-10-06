%load BW_G10.csv

figure();

plot(Freq,Phase,'*');

hold on

grid on

x=0:100:10^6;

A=160000;
b=11;

w0=6;

y=180/pi*atan(-x/((1+A*b)*w0));

plot(x,y);

