% Define your input data as an array of structs
subjects = [
    struct('name', 'Glimpses of Glorious India', 'total', 23, 'attended', 20);
    struct('name', 'Coding Classes', 'total', 4, 'attended', 2);
    struct('name', 'Object Oriented Programming', 'total', 46, 'attended', 43);
    struct('name', 'User Interface Design', 'total', 36, 'attended', 32);
    struct('name', 'Discrete Mathematics', 'total', 50, 'attended', 47);
    struct('name', 'Linear Algebra', 'total', 47, 'attended', 42);
    struct('name', 'Manufacturing Practice', 'total', 31, 'attended', 27);
    struct('name', 'Modern Physics', 'total', 32, 'attended', 28)
];


fprintf('Attendance Analysis:\n\n');

for i = 1:length(subjects)
    subj = subjects(i);
    total = subj.total;
    attended = subj.attended;
    
    fprintf('Subject: %s\n', subj.name);
    
    if attended > total
        fprintf('  Error: Attended classes (%d) > Total classes (%d)\n\n', attended, total);
        continue;
    end
    
    current_percentage = (attended / total) * 100;
    fprintf('  Current Attendance: %.2f%%\n', current_percentage);
    
    if current_percentage <= 75
        fprintf('  You cannot skip any more classes. Attendance is at or below 75%%.\n\n');
        continue;
    end

    % Calculate how many more classes can be skipped
    skippable = 0;
    while (attended / (total + skippable + 1)) > 0.75
        skippable = skippable + 1;
    end
    
    fprintf('  You can skip %d more class%s\n\n', ...
        skippable, ternary(skippable == 1, '', 'es'));
end

% Ternary helper function for pluralization
function out = ternary(cond, val_true, val_false)
    if cond
        out = val_true;
    else
        out = val_false;
    end
end
