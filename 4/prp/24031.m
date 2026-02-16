%% 1a) P(X=5) - Exactly 5
p1_a = binopdf(5, 10, 0.3)

% 1b) P(X=10) - Exactly 10
p1_b = binopdf(10, 10, 0.3)

% 1c) P(X<=2) - At most 2 (CDF)
p1_c = binocdf(2, 10, 0.3)

% 1d) P(X>8) - Greater than 8 (Complement of <= 8)
p1_d = 1 - binocdf(8, 10, 0.3)

%% 2a) Exactly 3 calls occupied (p=0.4)
p2_a = binopdf(3, 10, 0.4)

% 2b) At least one call NOT occupied
% Strategy: Use p_not = 0.6. We want P(X >= 1).
% This is 1 - P(X=0) (Total minus "None were free")
p2_b = 1 - binopdf(0, 10, 0.6)

% 2c) Expected number of occupied calls
% Formula: E[X] = n * p
expected_value = 10 * 0.4

%% Prob that human error is reason for exactly 2 accidents
p3 = binopdf(2, 4, 0.75)

% 4a) All 18 are ripe
p4_a = binopdf(18, 18, 0.9)

% 4b) At least 16 are ripe (X >= 16)
% Logic: 1 - P(X <= 15)
p4_b = 1 - binocdf(15, 18, 0.9)

% 4c) At most 14 are ripe (X <= 14)
% Logic: Direct CDF
p4_c = binocdf(14, 18, 0.9)

%% Prob that exactly 5 dislike it
p5 = binopdf(5, 18, 0.2)

%% 6a) P(X=0)
p6_a = poisspdf(0, 5)

% 6b) P(X=2)
p6_b = poisspdf(2, 5)

% 6c) P(X<=11)
p6_c = poisscdf(11, 5)

% 6d) P(X>25) -> 1 - P(X<=25)
p6_d = 1 - poisscdf(25, 5)

lambda = 3;

%% 7i) Exactly 2 customers
p7_i = poisspdf(2, lambda)

% 7ii) 2 or more customers (X >= 2)
% Logic: 1 - P(X <= 1) (Everything except 0 and 1)
p7_ii = 1 - poisscdf(1, lambda)
