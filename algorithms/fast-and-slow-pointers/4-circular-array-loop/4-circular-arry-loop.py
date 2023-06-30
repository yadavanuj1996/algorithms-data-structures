"""
Circular Array Loop Problem

Statement
An input array, nums containing non-zero integers, is given, where the value at each index represents the number of places to skip forward (if the value is positive) or backward (if the value is negative). When skipping forward or backward, wrap around if you reach either end of the array. For this reason, we are calling it a circular array. Determine if this circular array has a cycle. A cycle is a sequence of indices in the circular array characterized by the following:

The same set of indices is repeated when the sequence is traversed in accordance with the aforementioned rules.
The length of the sequence is at least two.
The loop must be in a single direction, forward or backward.
It should be noted that a cycle in the array does not have to originate at the beginning. A cycle can begin from any point in the array.

Constraints:
- 1 ≤ nums.length ≤ 10^4
- -5000 <= nums[i] <= 5000
- nums[i] != 0

Test Cases (Check attached README file for better understanding of problem and test cases)
Input :
[1, 3, -2, -4, 1]
Output:
True
Explanation: 
Starting with the first element, 1, and move one step forward to 3.Then, continue by moving three steps forward to the last element,1, and finally return to the first element, 1, again.

Input :
[2, 1, -1, -2, 2]
Output:
False 
Explanation: Starting with any element, a loop cannot be formed. For example,starting with the first element 2, move two steps forward to -1 orstarting with the second element 1, move one step forward to -1.All other elements in the array follow the same pattern.
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(1)
Note: Check Iteration 1 solution (that one is also very easy to understand but it uses two pointers and not fast and slow pointer)
"""
def circular_array_loop(num):  
    # Write your code here
    size = len(num)
    for i in range(size):
        slow = fast = i
        forward = num[i] > 0
        
        while True:
            # Move pointer by 1
            slow = next_step(slow, num[slow], size)
            if is_not_cycle(num, slow, forward):
                break

            fast = next_step(fast, num[fast], size)
            if is_not_cycle(num, fast, forward):
                break

            fast = next_step(fast, num[fast], size)
            if is_not_cycle(num, fast, forward):
                break

            if slow == fast:
                return True

    return False



def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result = size+result
    
    return result
    

def is_not_cycle(nums, pointer, prev_direction):
    current_direction = nums[pointer] >= 0
    if not current_direction == prev_direction or abs(nums[pointer] % len(nums)) == 0:
        return True
    
    return False
    

"""
Steps of solution:
- Traverse the entire nums array using slow and fast pointers, starting from index 0.
- Move the slow pointer one time forward/backward and the fast pointer two times forward/backward.
- If loop direction changes at any point or taking a step returns to the same location, continue to the next element.
- If the direction does not change, check whether both pointers meet at the same node, if yes, then the loop is detected and return TRUE.
- Return FALSE if don’t encounter a loop after traversing the whole array.
"""

def main():
    arr = [1, 1, 1, 2]
    print(circular_array_loop(arr))

if __name__ == "__main__":
    main()



"""
Iteration 1

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def circular_array_loop(num):  
    # Write your code here
    slow = 0
    while slow < len(num):
        fast = slow
        while True:
            val = get_index(num[fast] + fast, len(num))
            # self loop
            if fast == val:
                slow = slow+1
                break
            
            if num[fast] + fast > len(num) and val > slow:
                slow = slow + 1
                break


            fast = val
            if fast == slow:
                return True
            elif (num[fast] > 0 and num[slow] < 0) or (num[fast] < 0 and num[slow] > 0):
                slow = slow + 1
                break
    
    return False

def get_index(n, size):
    if n < size and n >= 0:
        return n
    elif n < 0: 
        return get_index(n + size, size)
    else:
        return get_index(n-size, size)
    

"""