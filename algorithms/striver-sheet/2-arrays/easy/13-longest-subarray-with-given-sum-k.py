"""
Longest Sub-array With Sum K
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    i = 0
    j = 0
    curr_sum = a[0]
    result = 0
    size = len(a)
    while i < size and j < size and i <= j:
        if curr_sum == k:
            if j-i+1 > result:
                result = j-i+1

            j+=1
            if i < size and j < size:
                curr_sum = curr_sum  + a[j]
        elif curr_sum < k:
            j += 1
            if j < size:
                curr_sum += a[j]
        elif curr_sum > k:
            i += 1
            if i < size:
                curr_sum -= a[i-1]

    return result
