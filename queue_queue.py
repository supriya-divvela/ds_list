from queue import Queue
p=int(input("Enter maxsize of queue:"))
l=Queue(maxsize=p)
while(1):
    print("1)Enqueue\n2)Dequeue\n3)Exit")
    ch=int(input())
    if(ch==1):
        if l.full():
            print("Queue is Full")
        else:
            p=int(input("Enter element to enqueue:"))
            l.put(p)
    elif(ch==2):
        if not l.empty():
            print("The dequeued element is:",l.get())
        else:
            print("Queue is empty")
    else:
        break