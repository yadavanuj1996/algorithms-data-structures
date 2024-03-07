![Screenshot 2024-03-07 at 4 15 47 AM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/acd8d361-b759-4396-8f01-a31cf79877e4)

Algorithm Steps:
- Initially take two pointers, fast and slow. The fast pointer takes two steps ahead while the slow pointer will take a single step ahead for each iteration.
- We know that if a cycle exists, fast and slow pointers will collide.
- If the cycle does not exist, the fast pointer will move to NULL
- Else, when both slow and fast pointer collides, it detects a cycle exists.
- Take another pointer, say entry. Point to the very first of the linked list.
- Move the slow and the entry pointer ahead by single steps until they collide. 
- Once they collide we get the starting node of the linked list.
