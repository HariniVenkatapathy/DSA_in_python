class Node:
    """A class representing a node in a singly linked list."""
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def append(self, data):
        """Append a new node with the given data to the end of the list."""
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            return
        last_node = self.head
        while last_node.next:  # Traverse to the end of the list
            last_node = last_node.next
        last_node.next = new_node  # Link the new node

    def display(self):
        """Display the contents of the list."""
        current_node = self.head
        while current_node:  # Traverse the list
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # Indicate the end of the list

def main():
    linked_list = LinkedList()  # Create a new linked list
    while True:
        user_input = input("Enter a value to add to the linked list (or 'exit' to finish): ")
        if user_input.lower() == 'exit':
            break
        linked_list.append(user_input)  # Append the user input to the list

    print("The linked list is:")
    linked_list.display()  # Display the linked list

if __name__ == "__main__":
    main()
