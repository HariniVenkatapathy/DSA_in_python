class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def deletionatbegining(head):
    new_head=head.next
    del head
    curr=new_head
    while curr:
        print(curr.data,end=" -> ")
        curr=curr.next
    print("None")
def deletionatend(head):
    current=head
    while current.next.next:
        current=current.next
    del_node = current.next
    current.next = None
    del del_node
    curr=head
    while curr:
        print(curr.data,end=" -> ")
        curr=curr.next
    print("None")
def deletionatpoint(head,ele):
    current=head
    current = head
    while current and current.next:
        if current.next.data == ele:  # Check if the next node is the one to delete
            current.next = current.next.next  # Bypass the node to delete
            return head  # Return the head of the list
        current = current.next

    print(f"Element {ele} not found in the list.")
    return head
def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")  

if __name__ == "__main__":
    head=Node(0)
    head.next=Node(1)
    head.next.next=Node(2)
    head.next.next.next=Node(3)
    head.next.next.next.next=Node(4)
    deletionatbegining(head)
    deletionatend(head)
    deletionatpoint(head,2)
    display(head)
