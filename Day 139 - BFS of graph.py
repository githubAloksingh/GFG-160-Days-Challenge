#User function Template for python3
from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    
    def bfs_recursive(self,queue,visited,adj,result):
        if not queue:
            return
        current=queue.popleft()
        result.append(current)
        
        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor]=True
                queue.append(neighbor)
        self.bfs_recursive(queue,visited,adj,result)
    def bfs(self, adj):
        # code here
        V=len(adj)
        result=[]
        visited=[False]*V
        queue=deque()
        
        visited[0]=True
        queue.append(0)
        self.bfs_recursive(queue, visited,adj,result)
        return result


#{ 
 # Driver Code Starts
import sys


#Position this line where user code will be pasted.
def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())  # Number of vertices
        adj = []  # Adjacency list

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.bfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
