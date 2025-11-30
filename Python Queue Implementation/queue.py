class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the first item from the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        return None  # More professional than "Queue is empty"

    def peek(self):
        """Return the first item without removing it."""
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self):
        """Return current number of items in the queue."""
        return len(self.items)

    def is_empty(self):
        """Check whether the queue is empty."""
        return len(self.items) == 0
