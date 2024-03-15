"""
Find pairs with given sum in doubly linked list

Problem Link:
https://www.codingninjas.com/studio/problems/find-pairs-with-given-sum-in-doubly-linked-list_1164172

Statement
A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have 
reference to both the previous and the next nodes in the sequence of nodes.

You are given a sorted doubly linked list of size 'n', consisting of distinct positive integers,
and a number 'k'.
Find out all the pairs in the doubly linked list with sum equal to 'k'.

Constraints:
- 0 <= n <= 100000
- 1 <= data in any node <= 10^9
- 1 <= k <= 10^9

Test Case:
Sample input 1:
5
1 2 3 4 9
5


Sample output
[ [1,4], [2, 3] ]


"""

"""
Time Complexity: O(n), more precise O(2n) two iterations are required
Space Complexity: O(1), no extra space used (depending on no of items added in res array)
"""

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def findPairs(head: Node, k: int) -> [[int]]:

    # Write your code here.
    # Return boolean true or false.
    tail = head
    cur_node = head
    res = []
    while tail.next:
        tail = tail.next
    
    while cur_node != tail:
        val = cur_node.data + tail.data
        if val == k:
            res.append([cur_node.data, tail.data])
            tail = tail.prev
        elif val < k:
            cur_node = cur_node.next
        elif val > k:
            tail = tail.prev
    
    return res

