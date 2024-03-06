
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
    
    def traverse(self):
        for i in range(self.front,self.rear+1):
            print(self.Queue[i],end=' ')
Q=Queue(2)
Q.enqueue(10)
Q.enqueue(30)
Q.enqueue(20)
Q.traverse()


