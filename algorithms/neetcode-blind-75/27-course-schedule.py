"""
TC: O(V + E)
SC: O(V + E)

Cycle detection in a directed graph (DFS). If a node is revisited while still on
the current DFS path (visited but not yet completed) => cycle => cannot finish.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_graph = [[] for i in range(numCourses)]

        for item in prerequisites:
            main_course = item[0]
            pre_req_course = item[1]
            node_graph[main_course].append(pre_req_course)

        course_completed = [0] * numCourses

        def courseFinish(node: int, visited_nodes: List[int]) -> bool:
            if course_completed[node]:
                return True

            if not course_completed[node] and visited_nodes[node]:
                return False

            visited_nodes[node] = 1

            if len(node_graph[node]) == 0:
                course_completed[node] = True
                return True

            for adj_node in node_graph[node]:
                if not courseFinish(adj_node, visited_nodes):
                    return False

            course_completed[node] = True
            return True


        for item in range(numCourses):
            if not course_completed[item]:
                if not courseFinish(item, [0]*numCourses):
                    return False

        return True
