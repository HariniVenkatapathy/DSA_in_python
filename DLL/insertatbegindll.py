class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def insertatbegin(head,key):
    new_node=Node(key)
    if head is None:
        head=new_node
    new_node.next=head
    head=new_node
    current=head
    while current:
        print(current.data,end=" ")
        current=current.next
        
if __name__=="__main__":
    node1=Node(1)
    node2=Node(2)
    node3=Node(4)
    node4=Node(5)
    node5=Node(6)
    node1.next=node2
    node2.prev=node1
    node2.next=node3
    node3.prev=node2
    node3.next=node4
    node4.prev=node3
    node4.next=node5
    node5.prev=node4
    head=node1
    insertatbegin(head,0)
    
        
