import java.util.ArrayList;

public class one {
  public static <T extends Comparable<T>> T[][] CleanMatrix(T[][] matrix) {
    ArrayList<Integer> rows_to_clear = new ArrayList<Integer>();
    ArrayList<Integer> cols_to_clear = new ArrayList<Integer>();
    
    for(int i = 0; i < matrix.length; i++)
    {
      for(int j = 0; j < matrix[0].length; j++)
      {
        if(matrix[i][j].compareTo((T)(Integer)0) == 0)
        {
          rows_to_clear.add(i);
          cols_to_clear.add(j);
        }
      }
    }
    for(int i = 0; i < matrix.length; i++)
    {
      for(int j = 0; j < matrix[0].length; j++)
      {
        if(rows_to_clear.contains(i) || cols_to_clear.contains(j))
        {matrix[i][j] = null;}
      }
    }
    return matrix;
  }

  public static void main(String[] args) {
    Integer[][] arr =  {{0,1,2},{3,4,0},{7,7,7}};
    Integer[][] ans = CleanMatrix(arr);

    for(Integer[] row: ans)
    {
      for(Integer element: row)
      {
        System.err.print(element + " ");
      }
      System.err.println();
    }
  }

}
