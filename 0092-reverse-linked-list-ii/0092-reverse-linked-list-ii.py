# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if head==None:
            return None
        if left==right:
            return head
        
        t=head
        bef=None
        pos=1
        while(t!=None):
            if pos<left:
                bef=t
                t=t.next
                pos+=1
                continue
            break
        
        curr=t
        prev=None
        time=right-left+1
        while (time>0):
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
            time-=1
        t.next=curr
        if bef==None:
            return prev
        else:
            bef.next=prev 
            return head



        
           


        