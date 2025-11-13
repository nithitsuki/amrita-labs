%% 1. Initialization and Setup
% -------------------------------------------------------------------------
% It's good practice to start with a clean slate.
clc;         % Clears the text in the command window.
clear all;   % Deletes all variables from memory to prevent old data from interfering.
close all;   % Closes any open plot windows.


%% 2. Define the Boundaries of the Feasible Region for Plotting
% -------------------------------------------------------------------------
% We want to draw the area where we are allowed to search for a solution.
% This area is defined by our constraints: x>=0, y>=0, and x+y>=1.

% Create a smooth range of x-values for our plot lines.
% linspace(start, end, number_of_points) is great for making smooth lines.
x_range_for_plot = linspace(0, 2, 100);

% The constraint x + y >= 1 can be written as y >= 1 - x.
% This line defines the slanted boundary of our region.
% We use max(0, 1-x) because y also has to be >= 0.
y_boundary_slanted = max(0, 1 - x_range_for_plot);

% The constraint y >= 0 is simply the x-axis.
% We create a line of zeros that has the same number of points as our x_range.
y_boundary_horizontal = zeros(size(x_range_for_plot));


%% 3. Create the Plot and Visualize the Feasible Region
% -------------------------------------------------------------------------
% Now, let's draw what we've defined.

figure; % Open a new window for the plot.

% Plot the two boundary lines in blue ('b').
plot(x_range_for_plot, y_boundary_slanted, 'b', 'LineWidth', 2);
hold on; % Tell MATLAB to draw the next plot on top of this one, not in a new window.
plot(x_range_for_plot, y_boundary_horizontal, 'b', 'LineWidth', 2);

% Shade the feasible region in green ('g').
% The 'fill' command creates a polygon. We give it the coordinates that
% trace the border of our region: go forward along the top boundary, then
% come back along the bottom boundary.
% 'fliplr' means "flip left-to-right", which is needed to trace the border back.
fill([x_range_for_plot, fliplr(x_range_for_plot)], ...
     [y_boundary_slanted, fliplr(y_boundary_horizontal)], ...
     'g', 'FaceAlpha', 0.2); % 'FaceAlpha' makes the color semi-transparent.


%% 4. Find the Minimum Value Using a Grid Search
% -------------------------------------------------------------------------
% This is the core of the solution. We will test a grid of points
% and find which one gives the lowest 'z' while being inside the feasible region.

% Define our objective function z = x^2 + y^2.
% This is an "anonymous function", like a lambda or arrow function.
objective_function = @(x, y) x.^2 + y.^2;

% Create a grid of (x,y) points to test. We'll search in the box from (0,0) to (2,2).
% The step size 0.01 gives us a fine grid for a more accurate answer.
[grid_X, grid_Y] = meshgrid(0:0.01:2, 0:0.01:2);

% Calculate the 'z' value for every single point on our grid.
Z_values = objective_function(grid_X, grid_Y);

% --- This is the key step for applying the constraint ---
% We find all the points on the grid that are *outside* our feasible region.
% The condition for being outside is (X + Y < 1).
% Then, we set the 'z' value for all those points to 'NaN' (Not a Number).
% This effectively disqualifies them from our search for the minimum.
Z_values((grid_X + grid_Y) < 1) = NaN;

% Now, find the minimum 'z' value among all the valid (non-NaN) points.
% The (:) operator flattens the 2D grid into a single long column.
% The 'min' function automatically ignores NaN values.
[min_Z_value, linear_index_of_min] = min(Z_values(:));

% We found the minimum value, but we need to know *where* it happened.
% 'ind2sub' converts the "linear index" back into (row, column) coordinates.
[min_row, min_col] = ind2sub(size(Z_values), linear_index_of_min);

% Finally, use the (row, column) to get the (x,y) coordinates of our answer.
min_X_coord = grid_X(min_row, min_col);
min_Y_coord = grid_Y(min_row, min_col);


%% 5. Add the Solution and Final Touches to the Plot
% -------------------------------------------------------------------------

% Mark the minimum point on the plot with a red circle ('ro').
plot(min_X_coord, min_Y_coord, 'ro', 'MarkerSize', 10, 'LineWidth', 2);

% Add a text label next to the point to show its coordinates.
% 'num2str' converts a number to a string so we can build the label.
text_label = sprintf(' Minimum at (%.2f, %.2f)', min_X_coord, min_Y_coord);
text(min_X_coord, min_Y_coord, text_label, 'VerticalAlignment', 'bottom');

% Add labels, a title, and a legend to make the plot easy to understand.
xlabel('X-axis');
ylabel('Y-axis');
title('Minimizing z = x^2 + y^2 in a Feasible Region');
legend('Boundary: x+y >= 1', 'Boundary: y >= 0', 'Feasible Region', 'Minimum Point');
ylim([0, 2]); % Set the y-axis limits to match the x-axis.

hold off; % We are done adding things to this plot.