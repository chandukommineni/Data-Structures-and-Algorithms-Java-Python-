#Selection Sort 
def SelectionSort(a,n):
    
    #iterate theough elements 
    for i in range(0,n):

        min=i 
        
        #if min element found after i th element change to min to j 
        for j in range(i+1,n):

            if a[j]<a[min]:
                min=j 
        
        #swap the element at i th position with min element 
        a[min],a[i]=a[i],a[min]

     
    
    return arr 




arr=list(map(int,input('Enter space seperated values\n').split()))
print(SelectionSort(arr,len(arr)))