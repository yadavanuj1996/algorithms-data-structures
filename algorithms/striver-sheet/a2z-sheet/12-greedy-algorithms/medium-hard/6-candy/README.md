### Intuition
We will go from left to right and compare each value to it's left ratings and if the cur rating is greater than
it's left neighbour rating, we will increase it candy val 1 more than the left candy value

While we go from right to left in next iteration and compare each element rating with it's right neighbour
rating if the cur element rating is greater than right neighbour rating and it's candy value is less than
the right candy value (Note: it can be greater as we have set it in above iteration i.e., left to right)
then we will update it's candy value 1 greater than right neighbour candy value.

### Algorithm Steps
- Initialize an array `candy_arr` with length `n` (number of children) where each element is initially set to 1.
- Iterate through the `ratings` list from left to right.
  - If the current child's rating is greater than the previous child's rating and the number of candies assigned to the current child is less than the number of candies assigned to the previous child plus 1, update the number of candies assigned to the current child to be one more than the number of candies assigned to the previous child.
- Iterate through the `ratings` list from right to left.
  - If the current child's rating is greater than the next child's rating and the number of candies assigned to the current child is less than the number of candies assigned to the next child plus 1, update the number of candies assigned to the current child to be one more than the number of candies assigned to the next child.
- Return the sum of all elements in the `candy_arr` array, which represents the total number of candies distributed among the children.
