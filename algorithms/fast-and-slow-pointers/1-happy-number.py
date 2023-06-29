
"""
Statement
Write an algorithm to determine if a number n is a happy number.

We use the following process to check if a given number is a happy number:

- Starting with the given number n, replace the number with the sum of the squares of its digits.
- Repeat the process until:
    - The number equals 1 , which will depict that the given number n is a happy number.
    - It enters a cycle, which will depict that the given number n is not a happy number.
Return TRUE if n is a happy number, and FALSE if not.

Constraints
- 1 <= n <= 2^31-1
"""

"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""
def is_happy_number(n):
    slow = n 
    fast = sum_of_squared_digits(n)
    while not fast == 1:
        if fast == slow:
            return False
        
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))
        
    return True


# helper function to that will return sum of square of digits of a num ex:- 21 -> (2)^2 + (1)^2 = 4+1 = 5
def sum_of_squared_digits(n):
    result = 0
    while n > 0:
        result += (n % 10 ) ** 2
        n = n // 10
    
    return result



"""
Steps of solution:
- Initialise a variable slow with the input number and fast with the squared sum of the input number’s digits.
- If fast is not 1 and also not equal to slow, increment slow by one iteration and fast by two iterations. Essentially, set slow to Sum of Digits(slow) and fast to Sum of Digits(Sum of Digits(fast)).
- If fast converges to 1, return TRUE, otherwise return FALSE.
"""
