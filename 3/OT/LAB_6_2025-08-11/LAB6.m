% 23MAT206 – Optimization Techniques
% Lab Sheet-4
% Implementation of Fibonacci Search Methods and Golden Section Search for Single Variable Optimization Problem

%% Custom Functions

function [a, b, iterations] = fib_search(f, a, b, tol)
% Build Fibonacci numbers until last >= (b-a)/tol
fib_numbers = [1 1];
while fib_numbers(end) < (b-a)/tol
    fib_numbers(end+1) = fib_numbers(end) + fib_numbers(end-1);
end
n_fib = numel(fib_numbers);
% Initial interior points (x_lower < x_upper)
% The formulas are:
%   x_lower = a + (F_{n-2} / F_n) * (b - a)
%   x_upper = a + (F_{n-1} / F_n) * (b - a)
x_lower = a + fib_numbers(n_fib-2)/fib_numbers(n_fib)*(b-a);
x_upper = a + fib_numbers(n_fib-1)/fib_numbers(n_fib)*(b-a);
f_lower = f(x_lower);
f_upper = f(x_upper);
iterations = 0;
% Loop (avoid indices going below 1: stop at n-3)
for k = 1:(n_fib-3)
    iterations = k;
    if f_lower > f_upper
        a  = x_lower;
        x_lower = x_upper;
        f_lower = f_upper;
        x_upper = a + fib_numbers(n_fib-k-1)/fib_numbers(n_fib-k)*(b-a);
        f_upper = f(x_upper);
    else
        b  = x_upper;
        x_upper = x_lower;
        f_upper = f_lower;
        x_lower = a + fib_numbers(n_fib-k-2)/fib_numbers(n_fib-k)*(b-a);
        f_lower = f(x_lower);
    end
    if (b-a) < tol, break;end
end
fib_min_x  = (a + b)/2;
fib_min_f  = f(fib_min_x);
fprintf('\nFibonacci Search:\n');
fprintf('  Final interval: (%.6f, %.6f)\n',a,b);
fprintf('  Length: %.6f | Iterations: %d\n', b-a, iterations);
fprintf('  Approx min: x = %.6f, f(x) = %.6f', fib_min_x, fib_min_f);
end

function [a, b, iterations] = golden_section(f, a, b, tol)
phi = (1+sqrt(5))/2;
golden_ratio = 1/phi; % approx 0.618
x_lower = b - golden_ratio*(b-a);
x_upper = a + golden_ratio*(b-a);
f_lower = f(x_lower);
f_upper = f(x_upper);
iterations = 0;
while (b-a) >= tol
    iterations = iterations + 1;
    if f_lower > f_upper
        a  = x_lower;
        x_lower = x_upper;
        f_lower = f_upper;
        x_upper = a + golden_ratio*(b-a);
        f_upper = f(x_upper);
    else
        b  = x_upper;
        x_upper = x_lower;
        f_upper = f_lower;
        x_lower = b - golden_ratio*(b-a);
        f_lower = f(x_lower);
    end
end
gold_min_x  = (a + b)/2;
gold_min_f  = f(gold_min_x);

fprintf('\nGolden Section Search:\n');
fprintf('  Final interval: (%.6f, %.6f)\n',a,b);
fprintf('  Length: %.6f | Iterations: %d\n', b-a, iterations);
fprintf('  Approx min: x = %.6f, f(x) = %.6f\n', gold_min_x, gold_min_f);
end

%% Question Answers

% Question 1:
f1  = @(x) -4*(x.^3) + 100 + exp(x);
fprintf('\nQuestion 1: minimum of f(x) = -4*(x^3) + 100 + e^x on (3,8):\n');
fib_search(f1, 3, 8, 0.25);
golden_section(f1, 3, 8, 0.25);

% Question 2:
f2 = @(x) exp(x) - 2*x;
fprintf('\nQuestion 2: minimum of f(x) = exp(x) - 2x on [0,3]:\n');
fib_search(f2, 0, 3, 0.25);
golden_section(f2, 0, 3, 0.25);

% Question 3:
f3 = @(x) 1./(x+1) + x.^2;
fprintf('\nQuestion 3: minimum of f(x) = 1/(x+1) + x^2 on [0,2]:\n');
fib_search(f3, 0, 2, 0.25);
golden_section(f3, 0, 2, 0.25);

% Question 4:
f4 = @(x) (x >= 0 & x < 1).*(2*x + 3) + (x >= 1 & x <= 3).*((x-2).^2 + 1);
fprintf('\nQuestion 4: minimum of piecewise f(x) on [0,3]:\n');
fib_search(f4, 0, 3, 0.25);
golden_section(f4, 0, 3, 0.25);

% Question 5:
f5 = @(x) exp(-x.^2) + 0.1*x.^2;
fprintf('\nQuestion 5: minimum of f(x) = exp(-x^2) + 0.1x^2 on [-2,2]:\n');
fib_search(f5, -2, 2, 0.25);
golden_section(f5, -2, 2, 0.25);

% Question 6:
f6 = @(x) x.^2.*log(x+1) + 1./(x+1);
fprintf('\nQuestion 6: minimum of f(x) = x^2*log(x+1) + 1/(x+1) on [0,4]:\n');
fib_search(f6, 0, 4, 0.25);
golden_section(f6, 0, 4, 0.25);

% Question 7:
f7 = @(x) (x >= 0 & x < 2).*((x-1).^2 + 2) + (x >= 2 & x <= 4).*((x-3).^2 - 1);
fprintf('\nQuestion 7: minimum of piecewise f(x) on [0,4]:\n');
fib_search(f7, 0, 4, 0.25);
golden_section(f7, 0, 4, 0.25);
