'''
25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. 
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
'''


class ListNode(object):
     def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
     def __repr__(self):
          return f"{self.val}"

def arraytoLL(arr):
    ans = ListNode()
    dummy = ans
    for i in arr:
        ans.next = ListNode(i)
        ans = ans.next
    return dummy.next

def LLtoarraypoint(head):
     a = []
     while head:
          a.append(head)
          head = head.next
     return a
          

def printLL(head):
     while head:
         print(head.val)
         head = head.next

def list_length(head):
     k = 0
     while head:
          k +=1
          head = head.next
     return k
          

def reverseKGroup(head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if k == 1:
             return head
        b = LLtoarraypoint(head)
        z = len(b)//k
        for m in range(z):
             otherarray = b[m*k:m*k +k]
             otherarray = otherarray[::-1]
             for inf in range(len(otherarray)):
                  b[m*k + inf] = otherarray[inf]
        for i in range(len(b)-1):
             b[i].next = b[i + 1]
        b[-1].next = None
        return b[0]

head = [1,2,3,4,5] 
head = arraytoLL(head)
k = 2
printLL(reverseKGroup(head,k))