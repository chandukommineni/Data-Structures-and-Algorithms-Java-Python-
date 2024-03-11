import java.util.*;
public class BubbleSort {

    public static void bubbleSort(int arr[])
    {
        for(int i=0;i<arr.length;i++)
        {

            for (int j=i;j<arr.length-i;j++){

                if (arr[j]<arr[i])
                {
                    int temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }

            }

        }

    }

    public static void main(String[] args) {
        int[] arr={1,4,2,5};
        bubbleSort(arr);
        System.out.println(Arrays.toString(arr));
    }
    
}
