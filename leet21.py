# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None


    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node


    # Print the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


l1 = [1,2,4]
l2 = [1,3,4]
list1 = LinkedList() 
list2 = LinkedList()
for x in l1:
    list1.insertAtEnd(x)
for x in l2:
    list2.insertAtEnd(x)

list1.printLL()
list2.printLL()

list3 = Node(0)

while list1.data <
