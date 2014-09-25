R1 =  99.620
  dR1 =  0.1
R2 =  99350;
  dR2 =  10;
Rb =  99540;
  dRb =  10;

Vom =  0.37030
  dVom =    2.0000e-03
Vop =  -0.36270
  dVop =    2.0000e-03

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