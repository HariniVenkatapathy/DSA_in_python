class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def insertatafter(head,key,index):
    new_node=Node(key)
    curr=head
    while curr is not None:
        if curr.data==index:
            break
        curr=curr.next
        
  
    new_node.prev=curr
    new_node.next=curr.next
    curr.next=new_node
    
def print_list(head):
    curr = head
    while curr is not None:
        print(f" {curr.data}", end='')
        curr = curr.next
    print()

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
    insertatafter(head,3,2)
    print_list(head)
    
