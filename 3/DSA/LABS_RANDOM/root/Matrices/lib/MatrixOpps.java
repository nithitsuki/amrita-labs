package root.Matrices.lib;
import java.util.Scanner;;
public class MatrixOpps {
    
    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }

    public static int[][] getMatrix(Scanner sc) {
        int[][] output = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                output[i][j] = sc.nextInt();
            }
        }
        return output;
    }
}