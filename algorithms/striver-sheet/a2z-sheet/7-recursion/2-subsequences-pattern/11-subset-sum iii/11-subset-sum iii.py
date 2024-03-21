"""
Letter Combinations of a Phone Number

Problem Link:
https://leetcode.com/problems/letter-combinations-of-a-phone-number

Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not
map to any letters.

Constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].


Test Case:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

"""
Time complexity: O(2^9)
Space complexity: O(k)
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        n = len(digits)
        result = []
        
        def letter_combinations(index, cur_seq):
            if index == n:
                # if is used to handle the case of digits being empty ""
                if cur_seq:
                    result.append(cur_seq)

                return 
            
            for item in phone_dict[int(digits[index])]:
                letter_combinations(index+1, cur_seq+item)
        
        letter_combinations(0, "")
    
        return result

            

