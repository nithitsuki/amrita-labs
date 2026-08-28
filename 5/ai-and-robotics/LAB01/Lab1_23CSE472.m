R = rotz(0.6)
R'*R
R*R'
det(R)
inv(R) - R'
R1 = rpy2tr(0.3, pi/2, 0.5)
R2 = rpy2tr(0.8, pi/2, 1.0)
R1 - R2
tr2rpy(R1)
