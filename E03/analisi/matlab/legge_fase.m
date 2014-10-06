load 'BW_G10.csv';

figure();

grid on

plot(Freq,Phase,'*');

hold on

x=0:100:10^6;

A=160000;
b=11;

w0=8;

y=180*pi*arctan(x/(1+A*b)*w0);

plot(x,y);

