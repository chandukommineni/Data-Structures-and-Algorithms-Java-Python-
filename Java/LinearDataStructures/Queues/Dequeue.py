class Dequeue:

    def __init__(self,size):
        self.arr=[]
        self.size=size
        self.front=-1
        self.rear=-1 
    
    def enqueueRear(self,val=0):
        if self.rear==self.size-1:
            print("Overflow")

        elif self.front==-1 and self.rear==-1:
            self.front=0
            self.rear=0
            self.arr.append(val) 
            print(val," inserted")
        else:
            self.rear+=1
            self.arr.append(val)
            print(val," inserted")

    def dequeueFront(self):
        if self.front==-1:
            print("underflow")
        elif self.front==self.rear:
            print("element popped is ",self.arr[self.front])
            self.front,self.rear=-1
        else:
            print("element popped is ",self.arr[self.front])
            self.front+=1 
    
    def enqueueFront(self,val=0):
        if self.front==0:
            print("Insertion not posiible ")
        elif self.front==-1:
            self.front+=1
            self.rear+=1
            self.arr.append(val)
            print(val," inserted")
        else:
            self.front=self.front-1 
            self.arr.insert(self.front,val) 
            print(val," inserted")

    def dequeueRear(self):
        if self.rear==-1:
            print("Queue is Empty")
        elif self.front==self.rear:
            print("element popped is ",self.arr[self.rear])
            self.front=-1
            self.rear=-1 
        else:
            print("element popped is ",self.arr[self.rear])
            self.rear-=1 

    def traverse(self):
        if self.front==-1 and self.rear==-1:
            print([])
            return
        for i in range(self.front,self.rear+1):
            print(self.arr[i],end=' ')
        print()


size=int(input("Enter the size of Queue\n"))
Q=Dequeue(size)
while True :
    choice=int(input("Select the operation\n1.enqueueFront\n2.enqueueRear\n3.deqeueFront\n4.dequeueRear\n5.Traverse\n6.exit\n"))
    if choice==1:
        Q.enqueueFront(int(input("enter value to insert\n")))
    elif choice==2:
        Q.enqueueRear(int(input("enter value to insert\n")))
    elif choice==3:
        Q.dequeueFront()
    elif choice==3:
        Q.dequeueRear()
    elif choice==3:
        Q.traverse()
    else:
        break