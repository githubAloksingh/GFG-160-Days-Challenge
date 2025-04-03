#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsRecursive(self,node,adj,visited,result):
        visited[node]=True
        result.append(node)
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfsRecursive(neighbor,adj,visited,result)
    def dfs(self, adj):
        # code here
        V=len(adj)
        visited=[False]*V
        result=[]
        self.dfsRecursive(0,adj, visited, result)
        return result

#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())
        adj = []

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.dfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
