"""
Maximum XOR With an Element From Array

Problem Link:
https://leetcode.com/problems/maximum-xor-with-an-element-from-array/description/

Statement
You are given an array nums consisting of non-negative integers. You are also given a queries array, 
where queries[i] = [xi, mi].

The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not 
exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements
in nums are larger than mi, then the answer is -1.

Return an integer array answer where answer.length == queries.length and answer[i] is the answer to 
the i query.


Constraints:
- 1 <= nums.length, queries.length <= 10^5
- queries[i].length == 2
- 0 <= nums[j], xi, mi <= 10^9


Test Case:

Input: 
nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]

Output:
[3,3,7]

"""

"""
Time complexity: Time Complexity: O(N*(log(N)) + M*(log(M)))
Space Complexity: O(N+M)
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
    def maximizeXor(self, nums: list[int], queries: list[List[int]]) -> list[int]:
        trie = Trie()
        
        for i in range(len(queries)):
            queries[i].append(i)

        queries.sort(key=lambda x:x[1])
        nums.sort()

        result = [-1]*len(queries)
        old_index =0 

        for item in queries:
            limit = item[1]

            while old_index < len(nums) and nums[old_index] <= limit:
                trie.insert(nums[old_index])
                old_index += 1

            original_index = item[2]
            # trie is empty case
            if old_index == 0:
                result[original_index] = -1
            else:
                result[original_index] = trie.find_max_xor(item[0])
                
        return result