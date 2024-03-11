def Mergesort(arr):
  if len(arr)==1:
    return arr
  n=len(arr)//2
  l1=arr[:n]
  l2=arr[n:]
  l1=Mergesort(l1)
  l2=Mergesort(l2)
  return merge(l1,l2)
  
def merge(a,b):
  i=0 
  j=0
  c=[]
  
  while i<len(a) and j<len(b):
    if a[i]<=b[j]:
      c.append(a[i])
      i+=1 
    else:
      c.append(b[j])
      j+=1 
  while i<len(a):
    c.append(a[i])
    i+=1 
  while j<len(b):
    c.append(b[j])
    j+=1 
  return c 

arr=list(map(int,input("enter space seperated value").split()))

print(Mergesort(arr))

