# Node class
class Node:
# Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
        # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    def deleteNode(self, key):
        print("Delete node "+(str)(key))
    #write code here
        temp = self.head
        if (temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None 
                return
        while(temp is not None):
            if temp.data == key :
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d" %(temp.data)),
            temp = temp.next
    def printReverse(self):
        if self.head == Node:  
            return None  
  
        previous = None  
        current = self.head  
        after = current.next   
  
        while current:  
            # Reverse the link  
            current.next = previous  
            # Moving previous element to one ahead  
            previous = current  
            # Moving current one element ahead  
            current = after  
            # Moving one element ahead  
            if after:  
                after = after.next  
    
        self.head = previous  
        self.printList()
        '''prev = None 
        curr = self.head
        while(curr is not None):
            next=  curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        self.printList()'''

if __name__ == "__main__":
        llist = LinkedList()
        llist.push(7)
        llist.push(1)
        llist.push(3)
        llist.push(2)
        print ("Created Linked List: ")
        llist.printList()
        llist.deleteNode(1)
        print ("Linked List after Deletion of 1:")

        llist.printList()
        print ("Print  Revese  of Linked List ")
        llist.printReverse()