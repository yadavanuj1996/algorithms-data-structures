# Algorithms and Data structure implementation using python
- List
- Linked List


```
                     			Big O growth
		 O(1)<O(log n) < O(sqrt n) < O(n) < O(n log n) < O(n^2) < O(a^n) < O(n!)
		 
Growth of several common time complexities, and thus help you judge if your algorithm is fast enough to get  Accepted  
		 Length Of Input(N)	 Worst Accepted Algorithm	   
		   <= [10..11]			O(N!), O(N^6)  
		   <= [15..18]			O(2^N * N^2)  
		   <= [18..22]			O(2^N * N)  
		   <= 100			O(N^4)  
		   <= 400			O(N^3)  
		   <= 2K			O(N^2 * log N)  
		   <= 10K			O(N^2)  
		   <= 1M			O(N * log N)  
		   <= 100M			O(N), O(log N), O(1)  
```

```
Rule of Thumb:
If there are T test cases multiply it to in left side while
Doing the analysis

1. N <= 10^6 -> O(N)/O(N log N)
2. N <= 10^5 -> O(N log^2 N)
3. N <= 10^4 -> O(N^2)/O(N log^2 N)
4. N <= 1000 -> O(N^2)/O(N^2 log N)
5. N <= 300/400-> O(N^3)
6. N <= 200 -> O(2^N))
7. N <= 15 -> O(N^2 2^N)
8. N <= 10 -> O(N!)
```
A computer can roughtly do 10^8 operations per second.

```
Some famous Sorting algorithms:-
	-Bubble Sort
	-Selection Sort
	-Insertion Sort
	-Merge Sort
	-Quick Sort
	-Counting Sort
	-Radix Sort
	-Heap Sort
	
	NOTE : REMOVE O(Big Oh) by Ω in best case and by θ(theta) in average case, the O is used
	I have used it in such way for easy memorization of table
	
```

                        Ω	        θ               O
                    Best Case   Average Case    Worst Case
	Bubble Sort     O(N)          O(N^2)          O(N^2)
	Insertion Sort  O(N)          O(N^2)          O(N^2)
	Selection Sort  O(N^2)        O(N^2)          O(N^2)
	Merge Sort      O(N log N)  O(N log N)        O(N log N)



### Python pre defined helper functions
```
- ord("a") returns 97 , the ord function takes a string value and returns the ASCII value of character.
- "a,bcd".find(",") => output 1
- "a" < "z", return true lexicographically comparsion
- ["z", "w", "p"].sort() , return the array in lexicographically sorted order. ["p", "w", "z"]
- '{:032b}'.format(3) , return '00000000000000000000000000000011' 32 bit binary string.
```

## 15 Leetcode articles I wish I'd read sooner.

- Backtracking Patterns: https://lnkd.in/g9csxVa4

- Sliding Window patterns: https://lnkd.in/gjatQ5pK

- Sliding Windows on Strings Pattern: https://lnkd.in/gX8ebtnb

- Two Pointers Patterns: https://lnkd.in/gBfWgHYe

- Substring Problem Patterns: https://lnkd.in/gdGtE72g

- Tree Patterns: https://lnkd.in/gKja_D5H

- Tree Iterative Traversal: https://lnkd.in/gGpXjHt5

- Dynamic Programming Patterns: https://lnkd.in/gbpRU46g

- Binary Search Patterns: https://lnkd.in/gKEm_qUK

- Monotonic Stack Patterns: https://lnkd.in/gdYahWVN

- Bit Manipulation Patterns: https://lnkd.in/gkxVZTXU

- Graph Patterns: https://lnkd.in/gKE6w7Jb

- DFS + BFS Patterns (1): https://lnkd.in/gPgpsgaQ

- DFS + BFS Patterns (2): https://lnkd.in/gd4ekfQe

- 14 Coding Interview Patterns: https://lnkd.in/gMZJVkFf



