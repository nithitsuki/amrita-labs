% NITHILAN RAMESHKUMAR - BL.SC.U4CSE24031

% 1 a) Print the homogeneous transformation matrix 3D if a rotation in y-axis
% by 29deg and translation of (12,1,8) has happened.
H = transl(12,1,8) * troty(29,'Deg');
disp(H)
% b) Print rotation from H in a). convert HTM to RPY 
tr2rt(H)
h2e(H)
tr2rpy(H)

% 2. assume manipulator at origin, the manipulator makes turn in following fashion

% a) turns by 83 deg in x-axis wrt movig frame
R1 = trotx(83,'deg');

% b) turns by 42 deg in y-axiis w.r.t fixed frame.
R2 = troty(42,'deg');

% Combined rotation:
R_final = R2 * R1;

% plot final rotation matrix. Form the pose matrix assuming a translation
% of (7,23,5).
T_start = eye(4)
T_end = transl(7,23,5) * R_final

% Create a random pose with random rotation and translation.
randR = rpy2tr(randn(1,3))
randT = transl(randn(1,3)*10)
T_rand = randT * randR

% animate between these two poses
figure;
ax = gca;
hold on;
view(3);
axis equal;
xlim([-20 20]); ylim([-20 30]); zlim([-10 20]);

n = 100;
Ts = trinterp(T_start, T_rand, linspace(0,1,n));

tranimate(Ts, 'frame', 'axes', 'trail', 'r', 'framesize', 1.5);

trplot(T_start, 'frame','s','rgb','length',1.5);
trplot(T_rand, 'frame','e','rgb','length',1.5);

hold off;