
"""
Minimum Number of Platforms

You have been given two arrays, 'AT' and 'DT', representing the arrival and departure times of all trains that
reach a railway station.

Your task is to find the minimum number of platforms required for the railway station so that no train needs 
to wait.

Note :
1. Every train will depart on the same day and the departure time will always be greater than the arrival time.
For example, A train with arrival time 2240 and departure time 1930 is not possible.

2. Time will be given in 24H format and colons will be omitted for convenience. For example, 9:05AM will be 
given as "905", or 9:10PM will be given as "2110".

3. Also, there will be no leading zeroes in the given times. For example, 12:10AM will be given as “10” and 
not as “0010”.

Constraints:
- 1 <= T <= 10
- 1 <= N <= 50000
- 0 <= AT[i] <= DT[i] <= 2359, Where 'AT[i]' and 'DT[i]' are the elements of the arrival and the departure arrays respectively.
- Time limit: 1 sec


Test Case:

Sample Input 1:
2

6
900 940 950 1100 1500 1800
910 1200 1120 1130 1900 2000
4
100 200 300 400
200 300 400 500

Sample Output 1:
3
2

"""



"""
Greedy Approach
Time Complexity: O(N log N), actually O(2N log N) + O(2N) ( we have skipped the O(N) part as it is lower)
Space Complexity: O(1)

"""
def calculateMinPatforms(at, dt, n):
    # Write your code here.
    at.sort()
    dt.sort()
    cur_plat, max_plat = 0, 0
    arr_index, dep_index = 0, 0

    while arr_index < n:
        while at[arr_index] > dt[dep_index]:
            cur_plat -= 1
            dep_index += 1
        
        cur_plat += 1
        max_plat = cur_plat if cur_plat > max_plat else max_plat
        arr_index += 1
    print(max_plat)
    