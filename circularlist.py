class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def pri(head):
    temp = head
    if head is not None:
        while(True):
            print (temp.data, end=" ")
            temp = temp.next
            if (temp == head):
                break 
    print()
head=last=None
while(1):
    print("1)Enter element to insert\n2)Enter element to insert at any position")
    ch=int(input())
    if(ch==1):
        ptr1 = Node(int(input("Enter element:")))
        temp=head
        ptr1.next = head
        if head is not None:
            while(temp.next !=head):
                temp = temp.next 
            temp.next = ptr1
        else:
            ptr1.next = ptr1
        head = ptr1
        pri(head)
    elif(ch==2):
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