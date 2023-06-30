# Find The Duplicate Number Problem

### Statement:
Given an unsorted array of positive numbers, nums, such that the values lie in the range  [1,n], inclusive, and
that there are n+1 numbers in the array, find and return the duplicate number present in nums. 
There is only one repeated number in nums.

#### Important Note: You cannot modify the given array nums. You have to solve the problem using only constant extra space.

### Constraints:
- 1 ≤ n ≤ 10^5
- nums.length = n+1
- 1 <= nums[i] <= n 
- All the integers in nums are unique, except for one integer that will appear more than once.

#### Test Case (Please check readme as well):
Input:
[1, 3, 3, 4, 2, 5]
Output:
3



## Floyd's Tortoise and Hare (Cycle Detection)  

The idea is to reduce the problem to Linked List Cycle Problem

First of all, where does the cycle come from?
Let's use the function f(x) = nums[x] to construct the sequence:
x, nums[x], nums[nums[x]], nums[nums[nums[x]]], ....

Each new element in the sequence is an element in nums at the index
of the previous element.

If one starts from x = nums[0], such a sequence will produce a linked list
with a cycle.

The cycle appears because nums contains duplicates. The duplicate node
is a cycle entrance.

<img width="641" alt="Screenshot 2023-07-01 at 3 54 46 AM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/18e8a3b9-0733-4ba3-a8b3-d2ffa217b96d">

The part 1 will of the solution will find the loop but to find the entrance of the loop we will use Floyd Tortoise and Hare algo

Let’s return to the example we just discussed, using this graphical representation:




A graphical presentation of the array

<img width="641" alt="Screenshot 2023-07-01 at 3 58 03 AM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/dd6fbcba-fa9e-40d4-be55-f849e5e770b5">

7 is the intersection point where the slow and fast pointers will meet.

8 is the entry point of the cycle, which is our duplicate number.


The fast pointer is traversing two times faster than the slow pointer. This can be represented by the following equation:
**d(fast) = 2 d(slow)**

Here, d represents the number of elements traversed (or total steps taken).

<img width="584" alt="Screenshot 2023-07-01 at 4 00 17 AM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/92ce3916-70d5-44f4-bb23-e0ed7ee207be">


In the diagram above:

- Green represents the entry point of the cycle.
- Blue represents the intersection point.
- Yellow represents the starting point.
- F represents the steps taken from the starting point to the entry point.
- a represents the steps taken to reach the intersection point from the entry point.
- C represents the cycle length, in terms of the number of steps taken to go once around the cycle.

d (slow)= F+a
d (fast)= F + nC + a
Also,
d(fast) = 2 d(slow)
=> F +nC+a = 2*(F+a)

On simlifying we get
F = nC - a

Which means the steps between starting point (0) and entry point will be same as steps between intersection point and entry point.

<img width="587" alt="Screenshot 2023-07-01 at 4 04 05 AM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/d7f54e0b-185d-49a4-bcc6-9dd552f9b5ec">

As we can see, nC−a is, in fact, the distance from the intersection point back to the entry point. This illustrates why, when we move one pointer forward, starting at the intersection point, and another pointer from the starting point, the point where they meet is the entry point of the cycle.

