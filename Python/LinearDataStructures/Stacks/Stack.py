class Stack:
    def __init__(self,size=0):
        self.stack=[] 
        self.size=size
    
    #Insert the Element
    def push(self,val):
        if len(self.stack)==self.size:
            print('Stack is full .Stack will Overflow')
        else:
            self.stack.append(val)
            print(f'{val} Pushed')

    #Remove the Top Most element
    def pop(self):
        if len(self.stack)==0:
            print('No Elements to pop .Stack will UnderFlow')
        else:
            print("Element Popped is ",self.stack.pop()) 

    #Returns the Top Element of Stack
    def peep(self):
        return self.stack[-1]
    
    
n=int(input("enter the size of the Stack\n"))
stack=Stack(n)
while True:
    choice=int(input('select operation\n1.push\n2.pop\n3.peep\n4.exit\n'))
    if choice==1:
        stack.push(int(input('Enter the value to Push\n')))
    elif choice==2:
        stack.pop()
    elif choice==3:
        print('Top Element is ',stack.peep())
    else:
        break 
