from typing import List

class Solution:

    #Example 3:
    # Input: numCourses = 3, prerequisites = [[1,2],[0,2]]
# Output: true
    
       #Example 4:
    # Input: numCourses = 3, prerequisites = [[1,2],[0,2],[2,1]]
# Output: false
    
        
       #Example 4:
    #  0
    # 1 2

    # Input: numCourses = 3, prerequisites = [[1,2],[0,1],[2,0]]
# Output: false

    


    #Detect if there is a cycle in graph
    #Approach 1:
    #Modeling it as a graph
    #create Node class
    #Use a set called existing to store the list of current nodes
    #iterate through prerequisites
    #if prerequisites[i][0] doesn't exist in existing 
    #create Node with value = prerequisites[i][0]
    #c

        
       #Example 5:

    # Input: numCourses = 3, prerequisites = [[1,0],[2,1]]
# Output: true

 #Detect if there is a cycle
    #Approach 2:
    # if prerequisites.length > 0
    # Create graph in Adjacency List from List of lists
    # iterate through prerequisites
    #  adjList is a map with node: [list of neighbors]
    #   adjList = {} will map with int: List[int]

    # if node b already exists as key in adjList
    # add node a to values (list) of that key in adjList
    # else 
    #   add node: [list of neighbors] to map

    #Traverse through adjList using depth first search iteratively
    # get a node from adjList
    # dfsStack = []
    # firstNode = prerequisites[0][1]
    # dfsStack.append(firstNode)
    # while dfsStack:
    #   curr = dfsStack.pop()
    #   neighbors = adjList[curr]
    #   if neighbors:
    #       dfsStack.



    # currPair = {}
    # currPair[[prerequisites[i][0]] = [[prerequisites[i][1]]
    #   adjList.append

    #Use set to store visited nodes
    # iterate through prerequisites
    # if !visited.contains(prerequisites[i][0])
    # add value of prerequisites[i][0] to visited
    # else
    #   return false
    # if !visited.contains(prerequisites[i][1])
    # add value of prerequisites[i][1] to visited
    # else
    #   return false

    def buildGraph(self,  numCourses: int, prerequisites: List[List[int]]):
        adjList = [[] for _ in range(numCourses)]

        for nodea, nodeb in prerequisites:
            adjList[nodeb].append(nodea)

        return adjList

    def hasCycle(self, adjList, start):
        visited = set()          # Set to keep track of visited vertices
        stack = [start]          # Stack for DFS traversal
        while stack:
            vertex = stack.pop() # Pop a vertex from the stack
            if vertex not in visited:
                print(vertex)    # Process the vertex (e.g., print it)
                visited.add(vertex)
                    # Push adjacent vertices onto the stack
                for neighbor in reversed(adjList[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
            else:
                return True
        return False        

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses > 0:
            adjList = self.buildGraph(numCourses, prerequisites)
            print(adjList)
            return not self.hasCycle(adjList, prerequisites[0][1])
        return True
    
    def main(self):
        # expected1 = True 
        # actual1 = self.canFinish(2, [[1,0]])
        # assert expected1 == actual1, "failed test case 1"

        expected1 = False 
        actual1 = self.canFinish(2, [[1,0], [0,1]])
        assert expected1 == actual1, "failed test case 2"

        
        # expected1 = False 
        # actual1 = self.canFinish(2, [[1,0], [0,1]])
        # assert expected1 == actual1, "failed test case 2"

if __name__ == '__main__':
    Solution().main()