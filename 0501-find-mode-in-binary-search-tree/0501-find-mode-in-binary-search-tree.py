# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        prev = None
        count = 0
        max_count = 0

        def inorder(node):
            nonlocal prev, count, max_count

            if node is None:
                return

            inorder(node.left)

            if node.val == prev:
                count += 1
            else:
                count = 1

            if count > max_count:
                max_count = count
                ans.clear()
                ans.append(node.val)

            elif count == max_count:
                ans.append(node.val)

            prev = node.val

            inorder(node.right)

        inorder(root)

        return ans
        

        