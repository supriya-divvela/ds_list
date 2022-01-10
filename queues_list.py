l=[]
while(1):
    print("1)Enqueue\n2)Dequeue\n3)Get front item\n4)Get rear item\n5)Exit")
    ch=int(input())
    if(ch==1):
        p=int(input("Enter element to enqueue:"))
        l.append(p)
        print(*l)
    elif(ch==2):
        if len(l):
            print("The dequeued element is:",l.pop(0))
        else:
            print("No elements in Queue")
    elif(ch==3):
        if len(l):
            print(f"The Front element is:{l[1]}")
        else:
            print("No elements in Queue")
    elif(ch==4):
        if len(l):
            print(f"The Rear element is:{l[1]}")
        else:
            print("No elements in Queue")
    else:
        break