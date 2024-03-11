class Node:
    def __init__(self,val=0):
        self.val=val 
        self.next=None 

class Stack:
    def __init__(self):
        self.head=None 

    def push(self,val=0):
        if not self.head:
            self.head=Node(val)
        else:
            node=Node(val)
            node.next=self.head 
            self.head=node 
    
    def pop(self):
        if self.head==None:
            print("Stack is Empty") 
        else:
            print("Element popped is ",self.head.val)
            self.head=self.head.next 

    def peep(self):
        return self.head.val if self.head else None
    

    def traverse(self):
        temp=self.head 
        if not temp:
            print("Empty")
            return
    
        while temp:
            print(temp.val,end=' ')
            temp=temp.next 
        print() 

stack=Stack()
while True:
    choice=int(input('select operation\n1.push\n2.pop\n3.peep\n4.display\n5.exit\n'))
    if choice==1:
        stack.push(int(input('Enter the value to Push\n')))
    elif choice==2:
        stack.pop()
    elif choice==3:
        print('Top Element is ',stack.peep())
    elif choice==4:
        stack.traverse()
    else:
        break