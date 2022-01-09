class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def pri(head):
    if head is None:
        print("No Elements in the list")
    else:
        while(head):
            print(head.data,end=' ')
            head=head.next
        print()
head=last=None
while(1):
    print("1)Insert at beginning\n2)Insert at end\n3)delete at beginning\n4)delete at end\n5)Insert at any position")
    ch=int(input())
    if(ch==1):
        if last is None:
            head=Node(int(input("enter the element to insert at beginning:")))
            last=head
        else:
            first=Node(int(input("enter the element to insert at beginning:")))
            first.next=head
            head=first
            pri(head)
    elif(ch==2):
        if(head is None):
            head=Node(int(input("enter the element to insert at end:")))
            last=head
        else:
            last.next=Node(int(input("enter element to insert at end:")))
            last=last.next
        pri(head)
    elif(ch==3):
        if head is None:
            print("No elements in linked list")
        else:
            head=head.next
            pri(head)
    elif(ch==4):
        if (head is None or head.next is None):
            print("No elements in the list")
        else:
            last=head
            while(last.next.next!=None):
                last=last.next
            last.next=None
            pri(head)
    elif(ch==5):
        if head is None:
            head=Node(int(input("Enter element to insert:")))
            last=head
            pri(head)
        else:
            p=int(input("enter position to insert:"))
            c=0
            first=head
            flag=True
            while(c<p-2):
                try:
                    first=first.next
                    c+=1
                except:
                    print("Invalid Position")
                    flag=False
                    break
            if flag:
                second=Node(int(input("enter element to insert:")))
                second.next=first.next
                first.next=second
                pri(head)
    else:
        break
