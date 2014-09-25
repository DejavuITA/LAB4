R1=119.8;
R2=9911;
R3=99350;
sR1=0.1;
sR2=1;
sR3=10;
Ginv1=-R2/R1;
Ginv2=-R3/R1;
Gninv1=1+R2/R1;
Gninv2=1+R3/R1;
Vout1=-103.5;
Vout2=-1025;
sVout1=0.5;
sVout2=2;

sG_INV1 = sqrt((-1/R1)^2 * sR2^2 + (R2/R1^2)^2 * sR1^2);
sG_INV2 = sqrt((-1/R1)^2 * sR3^2 + (R3/R1^2)^2 * sR1^2);
sG_NINV1 =sG_INV1; 
sG_NINV2=sG_INV2;

V_INV1 = - Vout1 * R1 / R2 ;
V_INV2 = - Vout2 * R1 / R3;

V_NINV1= Vout1  * R1 / (R1 + R2);
V_NINV2= Vout2 * R1 / (R1 + R3);




 sV_INV1 = sqrt( (R1 * Vout1 / R2^2)^2 * sR2^2 + (-Vout1/R2)^2 * sR1^2 + (-R1/R2)^2 * sVout1^2 );
 sV_INV2= sqrt( (R1 * Vout2 / R3^2)^2 * sR3^2 + (-Vout2/R3)^2 * sR1^2 + (-R1/R3)^2 * sVout2^2 );
 
sV_NINV1 = sqrt( (R2*Vout1/(R1+R2)^2)^2 * sR2^2 + (-R1*Vout1/(R1+R2)^2)^2 * sR1^2 + (R1/(R1+R2))^2 * sVout1^2 );
sV_NINV2 = sqrt( (R3*Vout2/(R1+R3)^2)^2 * sR3^2 + (-R1*Vout2/(R1+R3)^2)^2 * sR1^2 + (R1/(R1+R3))^2 * sVout2^2 );

%%%%%%%


Vout1RC=-105.5;
Vout2RC=-1038;
sVout1RC=0.5;
sVout2RC=2;



V_INV1RC = - Vout1RC * R1 / R2 ;
V_INV2RC = - Vout2RC * R1 / R3;

V_NINV1RC = Vout1RC  * R1 / (R1 + R2);
V_NINV2RC = Vout2RC * R1 / (R1 + R3);

sV_INV1RC = sqrt( (R1 * Vout1RC / R2^2)^2 * sR2^2 + (-Vout1RC/R2)^2 * sR1^2 + (-R1/R2)^2 * sVout1RC^2 );
sV_INV2RC= sqrt( (R1 * Vout2RC / R3^2)^2 * sR3^2 + (-Vout2RC/R3)^2 * sR1^2 + (-R1/R3)^2 * sVout2RC^2 );

sV_NINV1RC = sqrt( (R2*Vout1RC/(R1+R2)^2)^2 * sR2^2 + (-R1*Vout1RC/(R1+R2)^2)^2 * sR1^2 + (R1/(R1+R2))^2 * sVout1RC^2 );
sV_NINV2RC = sqrt( (R3*Vout2RC/(R1+R3)^2)^2 * sR3^2 + (-R1*Vout2RC/(R1+R3)^2)^2 * sR1^2 + (R1/(R1+R3))^2 * sVout2RC^2 );





DeltaV_INV1 = -V_INV1+V_INV1RC
sDeltaV_INV1 =sqrt(sV_INV1^2+sV_INV1RC^2)

DeltaV_INV2 = -V_INV2+V_INV2RC
sDeltaV_INV2 =sqrt(sV_INV2^2+sV_INV2RC^2)

DeltaV_NINV1 =- V_INV1+V_INV1RC;
sDeltaV_NINV1 =sqrt(sV_INV1^2+sV_INV1RC^2);

DeltaV_NINV2 = -V_INV2+V_INV2RC;
sDeltaV_NINV2 =sqrt(sV_INV2^2+sV_INV2RC^2);

R_C=100000;
sR_C=0.1;

DeltaVcompatibile=R_C*10^-9;
