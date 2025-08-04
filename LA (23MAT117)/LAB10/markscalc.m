% MATLAB Script: Calculate Weighted Percentage Based on Marks and Credits

% Subject credits as per the image
credits = [4, 4, 4, 3, 3, 1, 2]; % Total = 21

% Prompt the user for marks out of 50 for each subject
subjects = {
    'Discrete Mathematics', 
    'Linear Algebra', 
    'Object Oriented Programming', 
    'Modern Physics', 
    'User Interface Design', 
    'Manufacturing Practice', 
    'Glimpses of Glorious India'
};

marks = zeros(1, 7);
for i = 1:7
    prompt = sprintf('Enter marks out of 50 for %s: ', subjects{i});
    marks(i) = input(prompt);
end

% Scale marks to a 100-point scale
scaled_marks = (marks / 50) * 100;

% Calculate weighted average
total_credits = sum(credits);
weighted_sum = sum(scaled_marks .* credits);
percentage = weighted_sum / total_credits;

fprintf('\nYour overall percentage (credit-weighted) is: %.2f%%\n', percentage);
