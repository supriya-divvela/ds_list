l=[]
while(1):
    print("1)Push\n2)Pop\n3)Peek\n4)exit")
    ch=int(input())
    if(ch==1):
        l.append(int(input("Enter element to push into stack:")))
        print(*l)
    elif(ch==2):
        if len(l):
            print(f"The popped element is {l.pop()}")
        else:
            print("Stack is empty")
    elif(ch==3):
        if len(l):
            print(f"The Peek element is {l[-1]}")
        else:
            print("Stack is empty")
    else:
        break