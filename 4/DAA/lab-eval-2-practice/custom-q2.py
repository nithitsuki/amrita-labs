# Given two arrays array_One[] and array_Two[] of same size N, rearrange the
# arrays such that the sum of product pairs is minimum, i.e.,
# SUM(A[i] * B[i]) for all i is minimum.
#
# Time complexity:
# - Brute Force Approach: O((N!)^2)
# - Greedy Algorithm: O(N log N)
#
# Example:
# array_One[] = {7, 5, 1, 4}
# array_Two[] = {6, 17, 9, 3}
#
# If arranged as:
# array_One[] = {1, 4, 5, 7}
# array_Two[] = {17, 9, 6, 3}
#
# Then:
# (17 * 1) + (9 * 4) + (6 * 5) + (3 * 7)
# = 17 + 36 + 30 + 21
# = 104
#
# The minimum sum of products is 104.