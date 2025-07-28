public class five {
    static void PrintLeaders(Integer[] arr)
    {
        int start_pointer = 0;
        int len = arr.length;
        while (start_pointer != len-1) {
            int largest_num = Integer.MIN_VALUE;
            int largest_num_index = 0;
            for(int i = start_pointer+1; i < len; i++)
            {
                if(arr[i] > largest_num)
                {
                    largest_num = arr[i];
                    largest_num_index = i;
                }
            }
            System.out.print(largest_num+", ");
            start_pointer = largest_num_index;
        }
        System.out.println();
    }


    public static void main(String[] args) {
        Integer[] arr = {16,17,3,4,5,3,1};
        PrintLeaders(arr);
    }
}