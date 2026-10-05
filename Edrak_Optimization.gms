* ==========================================
* مشروع إدراك - شركة RG ENERGY
* كود الأمثلة الموسع لشبكة توزيع معقدة (10 محطات فرعية)
* ==========================================

Sets
    i / n1*n10 /  * عشر عقد نموذجية لشبكة توزيع ذكية
    alias(i,j);

Parameters
    P_Demand(i)  / n1 0, n2 40, n3 50, n4 30, n5 60, n6 45, n7 35, n8 55, n9 40, n10 30 /
    R(i,j)        / n1.n2 0.04, n2.n3 0.05, n3.n4 0.03, n4.n5 0.04, n5.n6 0.05, n6.n7 0.03, n7.n8 0.04, n8.n9 0.05, n9.n10 0.04 /
    S_Max(i,j)    / n1.n2 300,  n2.n3 250,  n3.n4 200,  n4.n5 250,  n5.n6 200,  n6.n7 150,  n7.n8 200,  n8.n9 250,  n9.n10 150 /
;

Variables
    P_Flow(i,j)  
    V(i)         
    Losses       
;

Positive Variables V;

Equations
    Objective_Function     
    Voltage_Limits_Min(i)  
    Voltage_Limits_Max(i)  
    Power_Balance(i)       
;

Objective_Function.. 
    Losses =e= sum((i,j)$R(i,j), (P_Flow(i,j)**2) * R(i,j));

Voltage_Limits_Min(i).. V(i) =g= 0.95;
Voltage_Limits_Max(i).. V(i) =l= 1.05;

Power_Balance(i)..
    sum(j$R(i,j), P_Flow(i,j)) - sum(j$R(j,i), P_Flow(j,i)) =e= P_Demand(i);

Model EdrakGrid10 /all/;
Solve EdrakGrid10 using NLP minimizing Losses;
