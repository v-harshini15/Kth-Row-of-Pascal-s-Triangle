Problem Description
Given an index k, return the kth row of the Pascal's triangle.
Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.
Example:
Input : k = 3
Return : [1,3,3,1]
Note: k is 0 based. k = 0, corresponds to the row [1].
Note: Could you optimize your algorithm to use only O(k) extra space?

Start with an initial row [1].

Iterate from 1 to k to generate each element of the row.

Calculate the next element using the formula: new_element = previous_element * (k - i + 1) // i, where i is the current position in the row.

Append each new element to the row.

Return the resulting row.

In the example with k = 3, the algorithm generates the row [1, 3, 3, 1] as the output.
