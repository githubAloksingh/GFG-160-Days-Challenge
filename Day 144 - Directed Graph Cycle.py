
class Solution:
    def isCycleDFS(self,adj,u,visited,inRecursion):
        visited[u]=True
        inRecursion[u]=True
        for v in adj[u]:
            if not visited[v] and self.isCycleDFS(adj,v,visited,inRecursion):
                return True
            elif inRecursion[v]:
                return True
        inRecursion[u]=False 
        return False
    def isCycle(self, V, edges):
        # code here
        adj=[]
        for _ in range(V):
            adj.append([])
        for u, v in edges:
            adj[u].append(v)
            
        visited=[False]*V
        inRecursion=[False]*V
        for i in range(V):
            if not visited[i] and self.isCycleDFS(adj,i,visited,inRecursion):
                return True
        return False



#{ 
 # Driver Code Starts
from collections import deque


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")


if __name__ == "__main__":
    main()

# } Driver Code Ends
