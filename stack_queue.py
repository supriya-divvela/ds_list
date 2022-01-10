from queue import LifoQueue
l=LifoQueue(maxsize=int(input("Enter maxsize of a stack:")))
while(1):
    print("1)Push\n2)Pop\n3)exit")
    ch=int(input())
    if(ch==1):
        if(l.full()):
            print("Stack is full")
        else:
            l.put(int(input("Enter element to push into stack:")))
    elif(ch==2):
        if not l.empty():
            print(f"The popped element is {l.get()}")
        else:
            print("Stack is empty")
    else:
        break