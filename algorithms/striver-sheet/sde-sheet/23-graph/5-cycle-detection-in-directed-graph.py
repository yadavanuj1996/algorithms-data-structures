"""
Note: This problem is from original SDE sheet not a2z sheet

Course Schedule

Problem Link:
https://leetcode.com/problems/course-schedule/description/

Statement
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.



Test Case:

Input: 
numCourses = 2
prerequisites = [[1,0]]

Output:  
True

Input: 
numCourses = 2
prerequisites = [[1,0],[0,1]]

Output: 
False

"""

"""
Time complexity: O(V+E), explanation below
Space Complexity: O(V+E)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        node_graph = [[] for i in range(numCourses)]

        for item in prerequisites:
            main_course = item[0]
            pre_req_course = item[1]
            node_graph[main_course].append(pre_req_course)

        course_completed = [0]* numCourses

        def courseFinish(node: int, visited_nodes: list[int])->bool:
            if course_completed[node]: 
               return True
            
            if not course_completed[node] and visited_nodes[node]:
                return False
            
            visited_nodes[node] = 1

            if len(node_graph[node]) == 0:
                course_completed[node] = True
                print(node, end="->")
                return True
 
            for adj_node in node_graph[node]:
                if not courseFinish(adj_node, visited_nodes):
                    return False
            
            course_completed[node] = True
            print(node, end="->")
            return True


        for item in range(numCourses):
            if not course_completed[item]:
                if not courseFinish(item, [0]*numCourses):
                    return False
        
        return True


sol = Solution()
prerequisite = [ [0,4], [4,3], [4,2], [3,1] ]
print(sol.canFinish(5, prerequisite))

"""
Time complexity
- Building the node_graph: This takes O(E) time, where E is the number of prerequisites.

- DFS traversal in courseFinish function: In the worst case, it may visit each course and each prerequisite once, resulting in O(V + E) time complexity.

- Main loop iterating through each course: O(V) time.

- Combining these, the overall time complexity is dominated by the DFS traversal, so the final time complexity is O(V + E).

Space complexity explanation
- node_graph: O(V + E) - This represents the adjacency list for the graph, including both vertices (courses) and edges (prerequisites).
- course_completed: O(V) - This list keeps track of whether a course is completed.
- visited_nodes (used in the courseFinish function): O(V) - In the worst case, this list will have the same length as the number of courses.
- Additionally, the recursive call stack during DFS can contribute to the space complexity. In the worst case, it may go as deep as the number of courses, resulting in an extra O(V) space for the call stack.
- Considering all these factors, the overall space complexity of your code is O(V + E)

"""
