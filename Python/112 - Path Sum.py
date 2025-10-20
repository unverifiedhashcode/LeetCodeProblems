# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recurse(currNode, currSum, targetSum):
    if currNode == None:
        return False

    
    currSum += currNode.val
    #print('at node',currNode.val,'with sum',currSum)

    if currSum == targetSum and currNode.left is None and currNode.right is None:
        #print('true!')
        return True
    
    res = recurse(currNode.left, currSum,targetSum)
    res = res or recurse(currNode.right, currSum,targetSum)
    return res


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return(recurse(root,0,targetSum))
