arr=list(map(int,input('enter space seperated values\n').split()))

def linearSearch(arr):
        flag=False
        val=int(input("enter value to search"))
        for i in range(len(arr)):
            if arr[i]==val:
                print(f'{val} is in {i} index')
                flag=True
        if not flag:
            print('element not exists')

while True:
    choice=int(input("1.search\n2.quit\n"))
    if choice==1:
         linearSearch(arr)

    else:
        break
