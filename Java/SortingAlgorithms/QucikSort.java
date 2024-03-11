import java.util.Arrays;

public class QucikSort {
    public static int partition(int[] arr,int low,int high){
        int i=low ;
        int j=high;
        int pivot=low;
        while (i<j)
        {
            while (arr[i]<=arr[pivot])
            {
                i++;
            }
            while (arr[j] > arr[pivot])
            {
                j--;
            }
            if (i<j){
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;

            }
        }

        int temp=arr[j];
        arr[j]=arr[pivot];
        arr[pivot]=temp;
        
        return j;

    }

    public static void quickSort(int[] arr,int low,int high)
    {   if (low<high)
        {
        int partionpoint=partition(arr,low, high);
        quickSort(arr,low,partionpoint-1);
        quickSort(arr, partionpoint+1, high);

         }


    }
    
    public static void main(String[] args) {
        int[] arr={1,4,2,5};
        quickSort(arr,0,arr.length-1);
        System.out.println(Arrays.toString(arr));

    }
}
