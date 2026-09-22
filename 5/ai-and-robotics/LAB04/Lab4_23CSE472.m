clear; clc; close all;

linkLen1 = 1;
linkLen2 = 1;
jointAngle1 = 0.2;
jointAngle2 = 0.3;

T_planar2_numeric = trchain2('R(q1),Tx(linkLen1),R(q2),Tx(linkLen2)', ...
    [jointAngle1 jointAngle2]);
T_planar2_numeric

syms q1 q2 linkLen1 linkLen2
T_planar2_symbolic = trchain2('R(q1),Tx(linkLen1),R(q2),Tx(linkLen2)', ...
    [q1 q2]);
T_planar2_symbolic

syms q1 q2 q3 linkLen1 linkLen2 linkLen3
T_planar3_symbolic = trchain2( ...
    'R(q1),Tx(linkLen1),R(q2),Tx(linkLen2),R(q3),Tx(linkLen3)', ...
    [q1 q2 q3]);
T_planar3_symbolic

syms q1 q2 q3 q4 linkOff1 linkOff2 linkOff3 linkOff4
T_3d4_symbolic = trchain( ...
    'Rz(q1)Tz(linkOff1)Ry(q2)Tz(linkOff2)Ry(q3)Tz(linkOff3)Ry(q4)Tz(linkOff4)', ...
    [q1 q2 q3 q4]);
T_3d4_symbolic

import ETS2.*
linkLen1 = 1;
linkLen2 = 1;

ets_planar2 = Rz('q1') * Tx(linkLen1) * Rz('q2') * Tx(linkLen2);
pose_planar2 = ets_planar2.fkine([30 40], 'deg');
structure_planar2 = ets_planar2.structure;
pose_planar2
structure_planar2

ets_planar2_prismatic = Rz('q1') * Tx(linkLen1) * Tx('q2');
structure_planar2_prismatic = ets_planar2_prismatic.structure;
structure_planar2_prismatic

pumaShoulderOffset = -0.2337;
pumaUpperArm = 0.4318;
pumaWristX = 0.0203;
pumaWristY = 0.0837;
pumaWristZ = 0.4318;
ets_puma560 = ETS3.Tz(0) * ETS3.Rz('q1') * ETS3.Ry('q2') * ...
    ETS3.Ty(pumaShoulderOffset) * ETS3.Tz(pumaUpperArm) * ETS3.Ry('q3') * ...
    ETS3.Tx(pumaWristX) * ETS3.Ty(pumaWristY) * ETS3.Tz(pumaWristZ) * ...
    ETS3.Rz('q4') * ETS3.Ry('q5') * ETS3.Rz('q6');
pose_puma560 = ets_puma560.fkine(zeros(1, 6));
pose_puma560

planar2Link1 = Link('revolute', 'd', 0, 'a', 1, 'alpha', 0);
planar2Link2 = Link('revolute', 'd', 0, 'a', 1, 'alpha', 0);
robot_planar2 = SerialLink([planar2Link1 planar2Link2], 'name', '2JointPlanar');
pose_robot_planar2 = robot_planar2.fkine(robot_planar2.toradians([30 40]));
robot_planar2.base = SE3(0, 0, 1);
robot_planar2
pose_robot_planar2

arm1Link1 = Link('revolute', 'd', 2, 'a', 1, 'alpha', pi/2);
arm1Link2 = Link('revolute', 'd', 0, 'a', 3, 'alpha', 0);
arm1Link3 = Link('revolute', 'd', 0, 'a', 1, 'alpha', 0);
arm1 = SerialLink([arm1Link1 arm1Link2 arm1Link3], 'name', 'ARM 1');
arm1

arm2Link1 = Link('revolute', 'd', 0, 'a', 3, 'alpha', pi/2);
arm2Link2 = Link('revolute', 'd', 0, 'a', 2, 'alpha', pi/2);
arm2Link3 = Link('prismatic', 'theta', 0, 'a', 1, 'alpha', pi/2, ...
    'qlim', [0 3], 'offset', 1);
arm2 = SerialLink([arm2Link1 arm2Link2 arm2Link3], 'name', 'ARM 2');
pose_arm2 = arm2.fkine(arm2.toradians([0 90 0]));
arm2
pose_arm2

planar3Link1 = Link('revolute', 'd', 0, 'a', 1, 'alpha', 0);
planar3Link2 = Link('revolute', 'd', 0, 'a', 1, 'alpha', 0);
planar3Link3 = Link('revolute', 'd', 0, 'a', 1, 'alpha', 0);
robot_planar3 = SerialLink([planar3Link1 planar3Link2 planar3Link3], ...
    'name', '3JointPlanar');

pose_tryout1 = robot_planar3.fkine([30 40 50], 'deg');
position_tryout1 = pose_tryout1.t;
pose_tryout1
fprintf('X = %.4f, Y = %.4f, Z = %.4f\n', position_tryout1(1), ...
    position_tryout1(2), position_tryout1(3));

pose_tryout2 = robot_planar3.fkine([15 45 55], 'deg');
position_tryout2 = pose_tryout2.t;
pose_tryout2
fprintf('X = %.4f, Y = %.4f, Z = %.4f\n', position_tryout2(1), ...
    position_tryout2(2), position_tryout2(3));
