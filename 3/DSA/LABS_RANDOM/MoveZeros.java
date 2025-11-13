public class MoveZeros {
    public static int[] moveZeros(int[] arr) {
        int[] newarr = new int[arr.length];
        int index = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 0) {
                newarr[index] = arr[i];
                index++;
            }
        }
                
        return newarr;
    }
    public static void main(String[] args) {
        int[] arr = {1,4,352,0,3,2,30,0,32,31,2};
        System.out.println("Zero Moved array is: ");
        for(int i: moveZeros(arr))
        {
            System.err.print(i+", ");
        }
        System.err.println();
    }
}
