R3=100000;
R4=5.2;

dR3=100;
dR4=0.1;

VA=0.88;
V_out=9.7;

dVA=0.03;
dV_out=0.2;


G=(V_out/VA)*(R4+R3)/R4

dG=sqrt(((1/VA)*(R4+R3)/R4)^2*dV_out^2 + ((V_out/VA^2)*(R4+R3)/R4)^2*dVA^2 + (V_out/(R4*VA))^2*dR3^2 + (V_out/(R4*VA) - ((R3 + R4)*V_out)/(R4^2*VA))^2*dR4^2  )



w0=6
wt101=10300
wt11=92000
dw0=0.2
dwt101=100
dwt11=1000
G11=11
dG11=0.1

G101=101
dG101=1


A11=G11/w0*(wt11-w0)

A101=G101/w0*(wt101-w0)


dA11=sqrt(
          (1/w0*(wt11-w0))^2*dG11^2+
          (G11*wt11/w0^2)^2*dw0^2+
          (G11/w0)^2*dwt11^2
          )

dA101=sqrt(
          (1/w0*(wt101-w0))^2*dG101^2+
          (G101*wt101/w0^2)^2*dw0^2+
          (G101/w0)^2*dwt101^2
          )
