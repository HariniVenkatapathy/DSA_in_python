class Node:
    def __init__(self,data):
        self.data= data
        self.next=None 
def insertionatbegin(head,ele):
    new_node=Node(ele)
    new_node.next=head
    head = new_node
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
def insertionatend(head,ele):
    new_node=Node(ele)
    current=head
    curr=head
    while current.next:
        current = current.next
    current.next= new_node
    while curr: # If the list is not empty, the function traverses the list until it finds the last node (the node whose next is None).
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")
def insertionatpoint(node,ele):
    new_node = Node(ele)
    new_node.next=node.next
    node.next=new_node
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
        
if __name__ =="__main__":
    head=Node(2)
    head.next=Node(3)
    head.next.next=Node(4)
    insertionatbegin(head,1)
    insertionatend(head,5)
    insertionatpoint(head,9)
