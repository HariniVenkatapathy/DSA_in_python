class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def iterate(head):
    current=head
    count=0
    while current:
        count+=1
        current=current.next
    print(count)
if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    iterate(head)
