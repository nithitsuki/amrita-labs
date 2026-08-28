H = transl(1,4,8) * trotx(45,'deg') * troty(70,'deg') * trotz(30,'deg')
R = t2r(H)
rpy = tr2rpy(R, 'deg')
[theta, v] = tr2angvec(R)
eul = tr2eul(R)
rpy2r(rpy, 'deg') - R
angvec2r(theta, v) - R
eul2r(eul) - R