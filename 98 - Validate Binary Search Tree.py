# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



def BSTValidRecurse(currNode, minVal,maxVal):
        if currNode == None:
            return True
        #print(currNode.val)
        if currNode.val < maxVal and currNode.val > minVal: #to be valid, currnode<parentNode
            #print('-')
            return(BSTValidRecurse(currNode.left,minVal, currNode.val) and BSTValidRecurse(currNode.right, currNode.val, maxVal))
        else:
            #print(minVal,'!<',currNode.val,'!<',maxVal)
            return False
        
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return(BSTValidRecurse(root,-2 ** 31 -1,2 **31 +1))
        