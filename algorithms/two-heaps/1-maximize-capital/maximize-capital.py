
"""
Maximize Capital

Statement
A busy investor with an initial capital, c, needs an automated investment program. They can select k distinct projects from a list of n projects with corresponding capitals requirements and expected profits. For a given project 
i, its capital requirement is capitals[i], and the profit it yields is profits[i].

The goal is to maximize their cumulative capital by selecting a maximum of k distinct projects to invest in, subject to the constraint that the investor’s current capital must be greater than or equal to the capital requirement of all selected projects.

When a selected project from the identified ones is finished, the pure profit from the project, along with the starting capital of that project is returned to the investor. This amount will be added to the total capital held by the investor. Now, the investor can invest in more projects with the new total capital. It is important to note that each project can only be invested once.

As a basic risk-mitigation measure, the investor wants to limit the number of projects they invest in. For example, if k is 2, the program should identify the two projects that maximize the investor’s profits while ensuring that the investor’s capital is sufficient to invest in the projects.

Overall, the program should help the investor to make informed investment decisions by picking a list of a maximum of k distinct projects to maximize the final profit while mitigating the risk.

Constraints:
- 1 ≤ k ≤ 10^5
- 0 ≤ c ≤ 10^9
- 1 ≤ n ≤ 10^5
- k ≤ n
- n == profits.length
- n == capitals.length
- 0 ≤ profits[i] ≤ 10^4
- 0 ≤ capitals[i] ≤ 10^9

Test Case:
Input:
n = 5, k = 3, c = 2
    
Capitals = [1, 3, 4, 5 ,6]
profits = [1, 2, 3, 4, 5]

Output:
Maximum Capital = 9
"""

from heapq import * 
"""
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
def maximum_capital(c, k, capitals, profits):
    size = len(capitals)
    capitals_min_heap = []
    profits_max_heap= []
    
    for i in range(size):
        capitals_min_heap.append((capitals[i], profits[i]))
    # creating a min heap of capital that contains profit in it as well to use later
    heapify(capitals_min_heap)
    for _ in range(k):
        # capitals_min_heap[0][0] represents peeking the min capital value in the heap that is root node of heap
        while capitals_min_heap and capitals_min_heap[0][0] <= c:
            # Pop min capital element and heapify the rest of the heap elements
            _, current_profit = heappop(capitals_min_heap)
            # push the profit to max heap of profits
            # inverting the value as max heap is not directly supported b
            # y heapq
            heappush(profits_max_heap, current_profit*-1)
            
        if not profits_max_heap:
            break

        # inverting the value as max heap is not directly supported by heapq
        pft = heappop(profits_max_heap) * -1
        c += pft
        
        

    return c
 
def main():
    """
    
    c = 0
    k = 1
    capitals = [1,1,2]
    profits = [1,2,3]
    """
    c = 1
    k = 3
    capitals = [1, 4, 2, 1]  
    profits = [2, 8, 5, 3]
    print(maximum_capital(c, k, capitals, profits))

if __name__ == "__main__":
    main()

