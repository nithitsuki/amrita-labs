import lib.MatrixOpps;

public class MatrixSearch {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        int Target = 5;
        System.out.println("Matrix:");
        MatrixOpps.printMatrix(matrix);


        boolean found = false;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (matrix[i][j] == Target) {
                    System.out.println("Value " + Target + " found at indices: [" + i + "][" + j + "]");
                    found = true;
                }
            }
        }

        if (!found) {
            System.out.println("Value " + Target + " not found in the matrix");
        }
    }
}
