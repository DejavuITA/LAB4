dvu1=16.14/2;
sdvu1=0.01;
dtu1=15.9;
sdtu1=0.1;

dvu2=12.96/2;
sdvu2=0.01;
dtu2=14.5;
sdtu2=0.1;

dvd=7.97/2;
sdvd=0.01;
dtd=11.4;
sdtd=0.1;




sru1=dvu1/dtu1 
dsru1=sqrt((1/dtu1)^2*sdvu1^2+(dvu1/dtu1^2)^2*sdtu1^2)
sru2=dvu2/dtu2 
dsru2=sqrt((1/dtu2)^2*sdvu2^2+(dvu2/dtu2^2)^2*sdtu2^2)
srd=dvd/dtd 
dsrd=sqrt((1/dtd)^2*sdvd^2+(dvd/dtd^2)^2*sdtd^2)