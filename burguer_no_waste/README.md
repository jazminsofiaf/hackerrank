# Matrix Linear ecuation Problem 

Suppose we have two integers tomatoSlices and cheeseSlices. These are the ingredients of different burgers −

Jumbo Burger: 4 tomato slices and 1 cheese slice.
Small Burger: 2 Tomato slices and 1 cheese slice.
We have to find [total_jumbo, total_small] so that the number of tomatoSlices that are left is equal to 0 and the number of cheeseSlices that are left is also 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return []. 

So if the input is tomatoSlices = 16 and chesseSlices = 7,
then the output will be [1, 6]. So this indicates, to make one jumbo burger and 6 small burgers, we need 4*1 + 2*6 = 16 tomatoSlices and 1 + 6 = 7 cheeseSlices


# Solution

this is a linear ecuation:

tomato =  4 total_jumbo + 2 total_small
cheese =  1 total_jumbo + 1 total_small

        b₁ = 4X₁ + Y₁
        b₂ = 2X₂ + Y₂

        (b₁ - Y₁)/4 = X₁
        (b₂ - Y₁)/2 = X₂


        b = A * x
  b * A-¹ = x

where 
* X Y is the solution to calculate
* b is given by the problem definition 
* A is a matrix 

A = [4  1]   
    [2  1]
A-¹ = 1 / det(A) * (Atraspuest) 

(if the det is 0 then is not inversible)

- det(A) = 4*1 -2*1 = 4-2 = 2
- A traspuesta = [1 -1]
                 [-2 4]

A-¹ = 1 / det(A) * (Atraspuest) 
A-¹ = 1 / 2 * [1 -1]
              [-2 4]
A-¹ = [1/2 -1/2]
      [-1    2 ]           

 b₁/2 -  b₂ = X₁
-b₁/2 + 2b₂ = Y₂

# input
tomato = 16 and chesse = 7
b = (16, 7)

# output

 16/2 - 7 = 8-7 = 1
-16/2 + 2*7 = -8 +14 = 6

x = (1, 6)





