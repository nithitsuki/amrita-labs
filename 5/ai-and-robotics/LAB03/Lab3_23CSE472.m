% Roll-Pitch-Yaw representation: R = Rz(yaw) * Ry(pitch) * Rx(roll)

% Singularity case - pitch = 90 degrees
% Keep (roll - yaw) constant this time, e.g. roll - yaw = -10

roll_a = 10; pitch_a = 90; yaw_a = 20;      % roll - yaw = -10
Ra = rotz(yaw_a,'deg') * roty(pitch_a,'deg') * rotx(roll_a,'deg')

roll_b = 30; pitch_b = 90; yaw_b = 40;      % roll - yaw = -10
Rb = rotz(yaw_b,'deg') * roty(pitch_b,'deg') * rotx(roll_b,'deg')

disp('Ra:'); disp(Ra)
disp('Rb:'); disp(Rb)
disp('Difference (Ra - Rb):')
disp(Ra - Rb)