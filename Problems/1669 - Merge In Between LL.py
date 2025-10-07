# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        aMinus = None
        bNode = None
        l2tail = None

        #l1
        currNode = list1
        listPos = 1
        while currNode.next is not None:
            #print(currNode.next.val,listPos)
            if aMinus == None and listPos == a: #breaks if not in, but a always in list they say
                aMinus = currNode
                #print('aMinus assigned')
            if bNode == None and listPos == b :
                #print('b assigned')
                b = currNode  

                
            currNode = currNode.next
            listPos+=1
        
        #l2
        l2tail = list2
        while l2tail.next is not None: #stop at tail
            l2tail = l2tail.next
        
        
        b = b.next #hack fix

        aMinus.next = list2
        bPlus = b.next
        b.next = None
        l2tail.next = bPlus


        return list1
