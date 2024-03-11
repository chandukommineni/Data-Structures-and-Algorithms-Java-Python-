def QuickSort(arr,low,high):

    if low<high:
        #taking pivot as starting element 
        pivot=low 
        i=low 
        j=high 
        #finding the correct position for pivot
        while i<j:

            while arr[i]<=arr[pivot]:
                i+=1 

            while arr[j]>arr[pivot]:
                j-=1 

            if i<j:

                arr[i],arr[j]=arr[j],arr[i] 
    
        arr[pivot],arr[j]=arr[j],arr[pivot]
        
        QuickSort(arr,low,j-1)
        QuickSort(arr,j+1,high)  
    

arr=list(map(int,input('Enter space seperated values ').split()))

QuickSort(arr,0,len(arr)-1)
print(arr)
