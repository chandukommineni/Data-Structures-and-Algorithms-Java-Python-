

#iterative approach
def BinarySearch(arr,n,val):
    low=0 
    high=n-1 
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==val:
            return mid 
        elif val<arr[mid]:
            high=mid-1 
        elif val>arr[mid]:
            low=mid+1
    return -1  

#recursive approach 
def Binary_Search(arr,low,high,val):
    if low<=high:

        mid = low + (high - low) // 2

        #if element is at mid location return mid
        if arr[mid]==val:
            return mid 
        
        #if the val is less than element at mid position go to left side of mid position element
        elif val<arr[mid]:
            return Binary_Search(arr,low,mid-1,val) 
        
        #if the val is less than element at mid position go to right side of mid position element
        elif val>arr[mid]:
            return Binary_Search(arr,mid+1,high,val)
        
    #it exectues when there is no element to search    
    else:
        return -1   

    

arr=list(map(int,input('enter space seperated sorted values\n').split()))
while True:
    choice=int(input("1.search\n2.other to quit\n"))
    if choice==1:
         val=int(input('enter the value to search\n'))
         ans=Binary_Search(arr,0,len(arr)-1,val)
         if ans==-1:
             print('element not found')
         elif ans:
             print(f'element found at {ans} index')

    else:
        break
