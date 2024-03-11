def BubbleSort(arr,n,choice):
    swapped=None

    #number of passes
    for i in range(0,n):
          
        #iterating the array 
        for j in range(1,n-i):

            swapped=False
            if choice==1:
                #if your previous value greater than current one. swap them
                if arr[j]<arr[j-1]:

                    arr[j],arr[j-1]=arr[j-1],arr[j] 

                    swapped=True 

            else:

                #if your previous value smaller than current one. swap them
                if arr[j]>arr[j-1]:

                    arr[j],arr[j-1]=arr[j-1],arr[j] 

                    swapped=True 


        #if the given array is already sorted no need go further
        if swapped==False:
           
            return arr 
    
    return arr 


while True:
    arr=list(map(int,input('Enter space seperated values\n').split()))
    print("choose the way of sorting \n1.Ascending\n2.Descending\n")
    choice=int(input())
    print('Befor Sorting : ',arr)
    print("After Sorting :",BubbleSort(arr,len(arr),choice))