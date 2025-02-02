from collections import deque
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
class Solution:
    def levelOrder(self, root):
        # Your code here
        if not root: 
            return []
        result=[]
        queue=deque()
        queue.append(root)
        
        while queue:
            level_size=len(queue)
            level_nodes=[]
            for i in range(level_size):
                node=queue.popleft()
                level_nodes.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        return result
        
