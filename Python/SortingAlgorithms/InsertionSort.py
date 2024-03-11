
def InsertionSort(a,n):

    for i in range(1,n):

        key=arr[i]
        j=i-1 

        while j>=0 and key<=a[j]:
            a[j+1]=a[j]
            j-=1 

        a[j+1]=key 
    return arr  

arr=list(map(int,input('Enter Space seperated values\n').split()))
print(InsertionSort(arr,len(arr)))