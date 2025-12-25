class HistoryEmptyError(Exception):
    """Custom exception for when the history has no items to process."""
    pass

class Task:
    """Represents a single node in the linked list history."""
    def __init__(self, description):
        if not description:
            raise ValueError("Task description cannot be empty")
        self.description = description
        self.next = None

class ActionHistory:
    """Manages the history of actions using a Singly Linked List."""
    def __init__(self):
        self.head = None
        self.size = 0

    def perform_action(self, description):
        """Adds a new action (Insertion at Head: O(1))."""
        try:
            new_task = Task(description)
            new_task.next = self.head
            self.head = new_task
            self.size += 1
            print(f"Action Performed: {description}")
        except ValueError as e:
            print(f"Failed to perform action: {e}")

    def undo_action(self):
        """Removes the most recent action (Deletion at Head: O(1))."""
        if self.head is None:
            raise HistoryEmptyError("Cannot undo: The action history is empty.")
        
        undone_task = self.head.description
        self.head = self.head.next
        self.size -= 1
        print(f"Undo Successful: {undone_task}")
        return undone_task

    def show_history(self):
        """Traverses the list to display actions (O(n))."""
        print("\n--- Current Action History ---")
        current = self.head
        if not current:
            print("History is empty.")
            return
            
        while current:
            print(f"[ {current.description} ]", end=" -> ")
            current = current.next
        print("End\n")

    def clear_history(self):
        """Instantly wipes history (O(1))."""
        self.head = None
        self.size = 0
        print("History cleared successfully.")

# --- App Execution with Error Handling ---
if __name__ == "__main__":
    history = ActionHistory()
    
    try:
        history.perform_action("Typed 'Hello World'")
        history.perform_action("Changed font to Bold")
        history.show_history()

        history.undo_action()
        history.undo_action()
        
        # This one will trigger our custom Exception
        history.undo_action() 
        
    except HistoryEmptyError as e:
        print(f"Alert: {e}")