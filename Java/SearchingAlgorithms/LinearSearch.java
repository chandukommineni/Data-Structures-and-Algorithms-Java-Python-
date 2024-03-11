package searching_algo;
import java.util.Scanner;
public class LinearSearch {
    public static  void Search(int[] arr,int size,int val){
        boolean flag=false;
        
        for(int i=0;i<size;i++)
        {
            if (arr[i]==val){
                System.err.println("element is at "+i+" index");
                flag=true;
            }
        }
        if (!flag){
            System.out.println("element not found");
        }

        
    }



    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        System.out.println("enter the size of the Array");

        int size=sc.nextInt();

        int[] arr=new int[size];

        for (int i=0;i<size;i++){
            arr[i]=sc.nextInt();
        }

        while(true){
            System.out.println("1.enter element to search\n 2.quit\n");
            int choice=sc.nextInt();
            if (choice==1){
                System.out.println("enter value to search\n");
                int val=sc.nextInt();
                Search(arr,size, val);
            }
            else{
                break;
            }
        }
        sc.close();

        
    }
}


