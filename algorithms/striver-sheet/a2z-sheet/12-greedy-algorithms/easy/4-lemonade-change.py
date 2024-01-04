"""
Problem Link:
https://leetcode.com/problems/lemonade-change

Time Complexity: O(N)
Space Complexity: O(1)
"""
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        result = True
        bill_count_dict = val = {5: 0, 10:0, 20:0}

        # Add the curr bill in a bill count dict that contains total no of notes available with lemoade stand
        for cur_bill in bills:
            bill_count_dict[cur_bill] = bill_count_dict[cur_bill] + 1

            # Code to count and return the change to customer
            if cur_bill == 10:
                if bill_count_dict[5] < 1:
                    result = False
                    break 
                else:    
                    bill_count_dict[5] -= 1
            elif cur_bill == 20:
                if bill_count_dict[10] >=1 and bill_count_dict[5] >=1:
                    bill_count_dict[5] -= 1
                    bill_count_dict[10] -= 1
                elif bill_count_dict[5] >= 3:
                    bill_count_dict[5] -= 3
                else:
                    result = False
                    break 
        
        return result
