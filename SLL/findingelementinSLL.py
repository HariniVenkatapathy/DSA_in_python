class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def finding_element(head,target):
    current_node = head
    while current_node:
        if current_node.data == target:
            print("The element is present")
            return 
        current_node = current_node.next
    print("The element is not present")
    
if __name__ == "__main__":
    head =Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    finding_element(head,3)
