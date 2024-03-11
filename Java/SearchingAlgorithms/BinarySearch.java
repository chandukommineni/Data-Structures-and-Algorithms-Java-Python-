import java.util.Scanner;

class BinarySearch{

    public static int binarysearch(int arr[],int low,int high,int target){

        while (low<=high){
            int mid=(low+high)/2;
            if (target==arr[mid]){
                return mid;
            }
            else if (target<arr[mid]){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
    
        }
        return -1;
    }



    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the size of the array");
        int size=sc.nextInt();
        int[] arr=new int[size];
        for(int i=0;i<size;i++)
        {
          arr[i]=sc.nextInt();
        } 
        while (true){
            System.out.println("enter the element to search or 0 to stop");
            int target=sc.nextInt();
            if (target==0) break; 
            int result=binarysearch(arr, 0, size-1, target); 
            if (result==-1){
                System.out.println("Element not Found");
            }
            else {
                System.out.println("Elemnt is at "+result+"\tlocation");
            }

        }
        sc.close();
        
    }
}