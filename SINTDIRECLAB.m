% Funcion de transferencia de Planta
Y = tf([10],[2 1])

% Funcion de transferencia de controlador PID
Kc1 = 0.2;
t11 = 1;
td1 = 0;

Gc1 = Kc1 + tf([Kc1],[t11 0]) + tf([Kc1*td1 0],[1])

% Funcion de transferencia a Lazo Cerrado
G_CL1 = Y*Gc1/(1+Y*Gc1);
[y1,td1] = step(G_CL1);

% Funcion de transferencia de controlador PID
Kc2 = 0.1;
t12 = 2;
td2 = 0;

Gc2 = Kc2 + tf([Kc2],[t12 0]) + tf([Kc2*td2 0],[1])

% Funcion de transferencia a Lazo Cerrado
G_CL2 = Y*Gc2/(1+Y*Gc2);
[y2,td2] = step(G_CL2);



plot(td1,y1,'g.')
hold on
plot(td2,y2,'b.')
hold on
grid
axis square
ylabel('y(t)')
xlabel('Time (s)')



