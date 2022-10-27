# Problem
Given a number K, find the smallest Fibonacci number ( other than 1 ) that shares a common factor with it. A number is said to be a common factor of two numbers if it exactly divides both of them. 

Output two separate numbers, F and D, where F is the smallest fibonacci number and D is the smallest number other than 1 which divides K and F.

(the Fibonacci numbers, form the Fibonacci sequence, in which each number is the sum of the two preceding ones.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144)

## Input Format 

First line of the input contains an integer T, the number of testcases.

Then follows T lines, each containing an integer K.

## Output Format

Output T lines, each containing the required answer for each corresponding testcase.

##  Sample Input

3

3

5

161

## Sample Output

3 3

5 5

21 7

## Explanation

There are three testcases. The first test case is 3, the smallest required fibonacci number  3. The second testcase is 5 and the third is 161. For 161 the smallest fibonacci numer sharing a common divisor with it is 21 and the smallest number other than 1 dividing 161 and 7 is 7.

## Constraints:

1 <= T <= 5

2 <= K <= 1000,000

The required fibonacci number is guranteed to be less than 10^18.