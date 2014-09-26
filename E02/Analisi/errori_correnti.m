R1 =  98.9
  dR1 =  0.1
R2 =  99400;
  dR2 =  100/10;
Rb =  99400;
  dRb =  100/10;

Vom =  3.89;
  dVom =    0.02;
Vop =  -3.72;
  dVop =    0.02;

[R1 R2 Rb Vom Vop]
[dR1 dR2 dRb dVom dVop]

Ibm = Vom* R1 / (R1*R2 + R1*Rb + R2*Rb)

dIbm = sqrt(
              ( (R1*Vom*(R1+Rb))/(R1*(R2+Rb)+R2*Rb)^2)^2 * dR1^2 +
              ( R2*Rb*Vom/(R1*(R2+Rb)+R2*Rb)^2)^2 * dR2^2 +
              ( R2*Rb*Vom/(R1*(R2+Rb)+R2*Rb)^2)^2 * dRb^2 +
              ( R1 / (R1*R2 + R1*Rb + R2*Rb))^2 * dVom^2
           )

Ibp = Vop * R1 / (Rb* (R1 + R2))

dIbp = sqrt(
              (R2*Vop / (Rb*(R1+R2)^2) )^2 * dR1^2 +
              (R1*Vop / (Rb*(R1+R2)^2) )^2 * dR2^2 +
              (R1*Vop / (Rb^2*(R1+R2)) )^2 * dRb^2 +
              (R1 / (Rb* (R1 + R2))    )^2 * dVop^2
           )

Ibp2 = (Ibm*R2 - Vop) * R1 / (Rb* (R1 + R2))
           
dIbp2 = sqrt(
              ( R2*(Ibm*R2 - Vop)/(Rb*(R1+R2)^2) )^2 * dR1^2 +
              ( R1*(Ibm*R1 + Vop)/(Rb*(R1+R2)^2) )^2 * dR2^2 +
              ( R1*(Vop - Ibm*R2)/(Rb^2*(R1+R2)))^2 * dRb^2 +
              (R1 / (Rb* (R1 + R2))    )^2 * dVop^2 +
              (R2 * R1 / (Rb* (R1 + R2)))^2 * dIbm^2
           )