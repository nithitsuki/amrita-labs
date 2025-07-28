import java.util.Arrays;
public class ShiftArray {
    static <T> T[] ShiftArrRightByK(T[] arr, int k)
    {
        int len = arr.length;
        k = k % len;
        int right_shifted = len - k;
        T[] newarr = Arrays.copyOf(arr, len);
        for(int i = k; i < len; i++)
        {
            newarr[i - k] = arr[i];
        }
        for(int i = right_shifted; i < len; i++)
        {newarr[i] = arr[i - right_shifted];}
        return newarr;
    }
    public static void main(String[] args) {
        Integer[] arr = {1,2,3,4,5};
        Integer[] ShiftedArr = ShiftArrRightByK(arr,3);
        System.out.println("Original array: " + Arrays.toString(arr));
        System.out.println("Shifted array: " + Arrays.toString(ShiftedArr));
    }    
}

// {1,2,3,4,5}
// len = 5;
// k = 3;
// {4,5,1,2,3}
