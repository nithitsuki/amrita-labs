%% ================================================================
%  23CSE472 - AI & Robotics Lab   Worksheet 1 - ANSWER KEY
%  ----------------------------------------------------------------
%  Same checks as Lab1_practice_fillme.m, all blanks filled.
%  Run sections with Ctrl+Enter and compare with your own answers.
%  ================================================================

n_fail = 0;

%% Section 1 - Rotation matrices
fprintf('\n== Section 1 : rotation matrices ==\n');

R90 = rot2(90,'deg');                        % [cos -sin; sin cos] at 90 deg
n_fail = n_fail + ~chk('Q1  rot2(90,''deg'') == [0 -1; 1 0]', ...
    norm(R90 - [0 -1; 1 0]) < 1e-10);

d = rotx(60,'deg') - rotx(pi/3);             % 60 deg == pi/3 rad
n_fail = n_fail + ~chk('Q2  rotx(60,''deg'') == rotx(pi/3)', ...
    norm(d, 'fro') < 1e-10);

R = rotz(0.6);
n_fail = n_fail + ~chk('Q3a  R''R  = I',    norm(R'*R  - eye(3), 'fro') < 1e-10);
n_fail = n_fail + ~chk('Q3b  det(R) = +1',  abs(det(R) - 1) < 1e-10);
n_fail = n_fail + ~chk('Q3c  inv(R) = R''', norm(inv(R) - R', 'fro') < 1e-10);

%% Section 2 - Visualizing frames (visual)
fprintf('\n== Section 2 : visualizing frames ==\n');
R45 = rot2(45,'deg');
figure; trplot2(R45, 'frame', 'A');          % x-tip (0.71,0.71), y-tip (-0.71,0.71)
R3 = rotx(60,'deg');
figure; trplot(R3, 'rgb');                   % x-axis stays put

%% Section 3 - Translation
fprintf('\n== Section 3 : translation ==\n');

T = transl2(2,3);
n_fail = n_fail + ~chk('Q6a  last column = (2,3)', ...
    norm(T(1:2,3) - [2; 3]) < 1e-12);
n_fail = n_fail + ~chk('Q6b  top-left 2x2 = identity', ...
    norm(T(1:2,1:2) - eye(2)) < 1e-12);

Tsum = transl2(2,3) * transl2(4,5);          % translations ADD
n_fail = n_fail + ~chk('Q7  transl2(2,3)*transl2(4,5) -> (6,8)', ...
    norm(Tsum(1:2,3) - [6; 8]) < 1e-12);

T3 = transl(1,4,6);
n_fail = n_fail + ~chk('Q8a  T3 is 4x4', all(size(T3) == [4 4]));
n_fail = n_fail + ~chk('Q8b  last column = (1,4,6)', ...
    norm(T3(1:3,4) - [1; 4; 6]) < 1e-12);

Hp = transl(1,2,3) * trotx(0.2);
p = Hp(1:3,4);                               % position = last column
n_fail = n_fail + ~chk('Q9  position extracted from Hp', ...
    norm(p - [1; 2; 3]) < 1e-12);

%% Section 4 - Homogeneous transforms
fprintf('\n== Section 4 : homogeneous transforms ==\n');

H = transl2(4,9) * trot2(70,'deg');          % THE pose line
n_fail = n_fail + ~chk('Q10a  top-left 2x2 = rot2(70,''deg'')', ...
    norm(H(1:2,1:2) - rot2(70,'deg')) < 1e-10);
n_fail = n_fail + ~chk('Q10b  origin = (4,9)', ...
    norm(H(1:2,3) - [4; 9]) < 1e-12);

Hord = trot2(70,'deg') * transl2(4,9);       % ORDER MATTERS
pexp = rot2(70,'deg') * [4; 9];              % origin swung to R*(4,9)
n_fail = n_fail + ~chk('Q11  origin got rotated: R*(4,9)', ...
    norm(Hord(1:2,3) - pexp) < 1e-12);

n_fail = n_fail + ~chk('Q12a  H''H ~= I (not orthogonal!)', ...
    norm(H'*H - eye(3), 'fro') > 0.1);
n_fail = n_fail + ~chk('Q12b  but inv(H)*H = I', ...
    norm(inv(H)*H - eye(3), 'fro') < 1e-10);
n_fail = n_fail + ~chk('Q12c  inv(transl2(2,3)) = transl2(-2,-3)', ...
    norm(inv(transl2(2,3)) - transl2(-2,-3)) < 1e-12);

H3 = transl(1,2,3) * troty(45,'deg');
n_fail = n_fail + ~chk('Q13a  origin = (1,2,3)', ...
    norm(H3(1:3,4) - [1; 2; 3]) < 1e-12);
n_fail = n_fail + ~chk('Q13b  rotation block = roty(45,''deg'')', ...
    norm(H3(1:3,1:3) - roty(45,'deg')) < 1e-10);

%% Section 5 - Animation (visual)
fprintf('\n== Section 5 : animation ==\n');
figure; tranimate2(transl2(3,2));            % slide only, no tilt
figure; tranimate(transl(1,2,3) * troty(45,'deg'));

%% Try-me 1 - orthogonal property
fprintf('\n== Try-me 1 : orthogonal property ==\n');
R = rotz(0.6);
prod1   = R'*R;                              % = I
prod2   = R*R';                              % = I
detR    = det(R);                            % = 1
diffIR  = inv(R) - R';                       % = 0
n_fail = n_fail + ~chk('T1a  R''R  = I', norm(prod1  - eye(3), 'fro') < 1e-10);
n_fail = n_fail + ~chk('T1b  RR''  = I', norm(prod2  - eye(3), 'fro') < 1e-10);
n_fail = n_fail + ~chk('T1c  det  = 1',  abs(detR - 1) < 1e-10);
n_fail = n_fail + ~chk('T1d  inv  = R''', norm(diffIR, 'fro') < 1e-10);

%% Try-me 2 - singularity / gimbal lock
fprintf('\n== Try-me 2 : singularity / gimbal lock ==\n');
roll1 = 0.3; roll2 = 0.8; pitch = pi/2; yaw1 = 0.5; yaw2 = 1.0;
R1 = rpy2tr(roll1, pitch, yaw1);             % (0.3, 90, 0.5)
R2 = rpy2tr(roll2, pitch, yaw2);             % (0.8, 90, 1.0)
n_fail = n_fail + ~chk('T2a  the triples really differ', ...
    (roll1 ~= roll2) && (yaw1 ~= yaw2));
n_fail = n_fail + ~chk('T2b  yet R1 == R2  ->  gimbal lock!', ...
    norm(R1 - R2, 'fro') < 1e-10);
% WHY: at pitch=pi/2 the matrix depends only on (yaw-roll) = 0.2 in BOTH.

R3 = rpy2tr(roll1, 0.5, yaw1);               % negative control:
R4 = rpy2tr(roll2, 0.5, yaw2);               % pitch=0.5 -> no collapse
n_fail = n_fail + ~chk('T2c  at pitch=0.5 the matrices differ', ...
    norm(R3 - R4, 'fro') > 0.1);

tr2rpy(R1)                                   % does NOT give back (0.3, 90, 0.5)!
% NOTE: if T2b FAILS, add the order option to rpy2tr: 'zyx' or 'xyz'.

%% Summary
fprintf('\n== Summary: %d check(s) failed (everything else PASSED) ==\n', n_fail);
if n_fail == 0
    fprintf('All checks PASSED - you are ready for the eval. Good luck!\n');
end

%% ------------------- local helper (do not edit) -------------------
function ok = chk(name, cond)
if cond
    fprintf('   [PASS] %s\n', name);
    ok = true;
else
    fprintf('   [FAIL] %s\n', name);
    ok = false;
end
end