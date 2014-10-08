load 'BW_G10.csv';
load 'BW_G100.csv';

% PLOT DELLE FASI

figure();

semilogx(BW_G10(1:length(BW_G10),1),BW_G10(1:length(BW_G10),4),'*');

hold on

semilogx(BW_G100(1:length(BW_G100),1),BW_G100(1:length(BW_G100),4),'*r');

grid on

% PRIMO PLOT

x1=0:10:10^6;

A1=160000;
b1=1/11;

w01=6;

y1=180/pi * atan(-x1/((1+A1*b1)*w01));

plot(x1,y1,'y');

% SECONDO PLOT

x2=0:10:10^6;

A2=160000;
b2=1/101;

w02=6;

y2=180/pi * atan(-x1/((1+A2*b2)*w02));

plot(x2,y2,'g');




% PLOT DEL GUADAGNO

figure();

semilogx(BW_G10(1:length(BW_G10),1),20*log10(BW_G10(1:length(BW_G10),3)/BW_G10(1:length(BW_G10),2)),'*');

hold on

semilogx(BW_G100(1:length(BW_G100),1),20*log10(BW_G100(1:length(BW_G100),3)/BW_G100(1:length(BW_G100),2)),'*r');

grid on

% TEORICA: (A^2 u^2)/((u + A b u)^2 + x^2)

% PRIMO PLOT

x3=0:10:10^6;

A3=160000;
b3=1/11;

w03=8;

y3=20*log10(sqrt((A3^2 * w03^2)./((w03 + A3*b3*w03)^2 + x3.^2)));

plot(x3,y3,'y');

% SECONDO PLOT

x4=0:10:10^6;

A4=160000;
b4=1/101;

w04=6;

y4=20*log10(sqrt((A4^2 * w04^2)./((w04 + A4*b4*w04)^2 + x4.^2)));

plot(x4,y4,'g');

clear