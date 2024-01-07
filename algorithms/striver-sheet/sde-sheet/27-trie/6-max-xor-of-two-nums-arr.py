"""
Maximum xor of two numbers in an array

Problem Link:
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/submissions/

Statement
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Constraints:
- 1 <= nums.length <= 2 * 10^5
- 0 <= nums[i] <= 2^31 - 1


Test Case:

Input: 
nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output : 127


Input: nums = [3,10,5,25,2,8]
Output: 28

"""

"""
Time complexity: O(N)     # O(N*32) insert + O(N*32) find xor max
Space Complexity: N/A
"""

class TrieNode:
    def __init__(self):
        self.links = [None]*2
    
    def contains_key(self, bit: int)->bool:
        return self.links[bit] is not None

    def get(self, bit: int)-> "TrieNode":
        return self.links[bit]
    
    def put(self, bit: int, node: "TrieNode")->None:
        self.links[bit] = node
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num: int):
        binary_str = '{:032b}'.format(num)
        node = self.root
        for cur_char in binary_str:
            cur_bit = int(cur_char)
            if not node.contains_key(cur_bit):
                node.put(cur_bit, TrieNode())

            node = node.get(cur_bit)
    
    def find_max_xor(self, num: int):
        binary_str = '{:032b}'.format(num)
        node = self.root
        result = ""
        for cur_char in binary_str:
            cur_bit = int(cur_char)
            reverse_bit = 1 - cur_bit   # 0 for 1 and 1 for 0, flipping the bit

            if node.contains_key(reverse_bit):
                result += "1"                # cur_bit^reverse_bit will alwasy give 1
                node = node.get(reverse_bit)
            else:
                result += "0"                 # cur_bit^cur_bit will alwasy give 0
                node = node.get(cur_bit)
            
        return int(result, 2)



class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)

        result = float("-inf")
        
        for num in nums:
            xor_val = trie.find_max_xor(num)
            if xor_val > result:
                result = xor_val

        return result
        