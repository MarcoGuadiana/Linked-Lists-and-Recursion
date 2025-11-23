class Node:
    

    def __init__(self, data):
       
        self.data = data
        self.next = None


class LinkedList:
    

    def __init__(self):

        self.head = None

    # --- Standard Insertion Methods (Iterative) ---

    def insert_at_front(self, data):
       
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # --- Recursive Methods ---

    def _sum_helper(self, node):
        
        if node is None:
            return 0
        return node.data + self._sum_helper(node.next)

    def recursive_sum(self):
        
        return self._sum_helper(self.head)

    def _reverse_helper(self, current, prev):
        
        # Base case: Reached the end of the original list. 'prev' is the new head.
        if current is None:
            return prev

        # Standard step: Save the next node before overwriting current.next
        next_node = current.next
        # Swap: Reverse the pointer
        current.next = prev
        # Recurse: Move one step forward
        return self._reverse_helper(next_node, current)

    def recursive_reverse(self):
        
        # The head is updated by the return value of the helper function
        self.head = self._reverse_helper(self.head, None)

    def _search_helper(self, node, target):
        
        # Base case 1: Target not found, reached the end
        if node is None:
            return False
        # Base case 2: Target found
        if node.data == target:
            return True
        # Recursive step: Move to the next node
        return self._search_helper(node.next, target)

    def recursive_search(self, target):
       
        return self._search_helper(self.head, target)

    # --- Display Method ---

    def display(self):
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")