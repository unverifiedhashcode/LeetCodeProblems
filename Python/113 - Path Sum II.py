# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recurse(currNode, currSum, targetSum, currPath, successPaths):
    #base case
    if currNode == None:
        return successPaths

    #calculations
    currSum += currNode.val
    currPath.append(currNode.val)
    #print('at node',currNode.val, 'with path',currPath,'and sum',currSum)
    #print('successpaths',successPaths)
    
    #recurse cases
    if currSum == targetSum and currNode.left is None and currNode.right is None:
        successPaths.append(currPath.copy())
        #print('Success! Adding',currPath)
        currPath.pop()
        return successPaths


    successPaths = recurse(currNode.left, currSum, targetSum, currPath, successPaths)
    successPaths = recurse(currNode.right, currSum, targetSum, currPath, successPaths)
    currPath.pop()
    return successPaths

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return(recurse(root, 0, targetSum,[],[]))
        
