
class Queue:
    def __init__(self,size=0) -> None:
        self.Queue=[]
        self.front=-1 
        self.rear=-1 
        self.size=size
    
    def enqueue(self,val=0):
        
        if self.rear==-1 and self.front==-1:
            self.front+=1 
            self.rear+=1 
            self.Queue.append(val)

        elif self.size==len(self.Queue[self.front:self.rear+1]):
            print('Queue is full') 
        else:
            self.Queue.append(val)
            self.rear+=1 
    def dequeue(self):
        if self.rear==-1:
            print("Queue is empty")
        elif self.front==self.rear:
            print('element popped is ',self.Queue[self.rear])
            self.front=-1 
            self.rear=-1 
        else:
            print('element popped is ',self.Queue[self.front])
            self.front+=1       
            
    def traverse(self):
        if self.front==-1 and self.rear==-1:
            print('queue is empty')
            return
        for i in range(self.front,self.rear+1):
            print(self.Queue[i],end=' ')
        print()

size=int(input("Enter the size of Queue"))
Q=Queue(size)
while True :
    choice=int(input("Select the operation\n1.enqueue\n2.dequeue\n3.traverse\n4.exit\n"))
    if choice==1:
        Q.enqueue(int(input("enter value to insert\n")))
    elif choice==2:
        Q.dequeue()
    elif choice==3:
        Q.traverse()
    else:
        break




