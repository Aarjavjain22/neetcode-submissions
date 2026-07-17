"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash={}
        def dfs(node):
            if node in hash:
                return hash[node]

            copy=Node(node.val)
            hash[node]=copy
            for x in node.neighbors:
                copy.neighbors.append(dfs(x))
            return copy
        if node:
            return(dfs(node))
        else:
            None

        