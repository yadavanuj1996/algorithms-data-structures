
"""
Add one to a number represented as Linked List

Problem Link:
https://www.codingninjas.com/studio/problems/add-one-to-a-number-represented-as-linked-list_920557

Statement
You're given a positive integer represented in the form of a singly linked-list of digits. 
The length of the number is 'n'.
Add 1 to the number, i.e., increment the given number by one.
The digits are stored such that the most significant digit is at the head of the linked list and the least 
significant digit is at the tail of the linked list.

Constraints:
- 1 <= 'n' <=  10^5
- 0 <= Node in linked list <= 9

Test Case:

Sample Input 1:
3
1 5 2


Sample Output 1:
1 5 3


Explanation For Sample Input 1:
Initially the number is 152. After incrementing it by 1, the number becomes 153.
"""


"""
Approach 1: 
Time complexity:  O(2), actually it's O(2N) as we are iterating twice
Space complexity: O(N)

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addOne(head: Node) -> Node:
    # write your code here
    cur_node = head
    val = ""
    while cur_node:
        val += str(cur_node.data)
        cur_node = cur_node.next
    
    cur_node = head
    prev = None
    for i in str(int(val)+1):
        if cur_node:
            cur_node.data = i
            prev = cur_node
            cur_node = cur_node.next
        else:
            prev.next = Node(i)
    
    return head
"""

"""
Approach 2: Using recursion (Better in terms of no tampering of data and in faster time although con is it uses extra space)
Time Complexity: O(N), We will iterate over the list once using recursion
Space Complexity: O(N), recursion stack space will cause it to O(N)
"""
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.
def addOne(head: Node) -> Node:

    def add_one_ll(cur_node):
        if not cur_node:
            return 1
        
        carry = add_one_ll(cur_node.next)
        val = carry + cur_node.data
        cur_node.data = 0 if val > 9 else val
        carry = 1 if val > 9 else 0
        return carry
    
    carry = add_one_ll(head)
    if carry:
        temp = Node(carry, head)
        head = temp
    
    return head
        

        
