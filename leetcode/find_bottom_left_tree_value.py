# source: https://leetcode.com/problems/find-bottom-left-tree-value/
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        deq = deque([root])

        last = None
        while deq:
            value = deq.popleft()
            last = value.val  # store popped node value

            left, right = value.left, value.right
            if right:
                deq.append(right)
            if left:
                deq.append(left)

        return last
