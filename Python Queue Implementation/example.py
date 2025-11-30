from queue import Queue

def main():
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Dequeued:", q.dequeue())  # 10
    print("Peek:", q.peek())         # 20
    print("Size:", q.size())         # 2
    print("Is empty:", q.is_empty()) # False

    q.dequeue()
    q.dequeue()

    print("After removing all items...")
    print("Is empty:", q.is_empty()) # True
    print("Peek:", q.peek())         # None

if __name__ == "__main__":
    main()
