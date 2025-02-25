
public class Feb11_arrays{
    @SuppressWarnings("all")
    static int fih = 20;
    public static void main(String[] args)
    {
        //1d arrays
      //int[]     a = new int[];          //error bcz new xx[number] requires atleast one value
        int[]     b = new int[3];
        //2d arrays
      //int[][]   c = new int[][];        //error same as above error
        int[][]   d = new int[3][];
      //int[][]   e = new int[][4];       //error cant do int[][x]
        int[][]   f = new int[3][4];
        //3d arrays
        int[][][] g = new int[3][4][5];
        int[][][] h = new int[3][4][];
      //int[][][] i = new int[3][][5];    //error
      //int[][][] k = new int[][3][4];    //error

        System.out.println(fih);
        int fih = 30;
        System.out.println(fih);
    }
}
