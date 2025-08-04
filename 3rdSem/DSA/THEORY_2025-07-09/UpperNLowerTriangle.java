import root.Matrices.lib.MatrixOpps;

public class UpperNLowerTriangle {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        int[][] upperTriangle = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i <= j) {
                    upperTriangle[i][j] = matrix[i][j];
                } else {
                    upperTriangle[i][j] = 0;
                }
            }
        }

        // Create lower triangular matrix
        int[][] lowerTriangle = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i >= j) {
                    lowerTriangle[i][j] = matrix[i][j];
                } else {
                    lowerTriangle[i][j] = 0;
                }
            }
        }

        System.out.println("\nUpper Triangular Matrix:");
        MatrixOpps.printMatrix(upperTriangle);

        System.out.println("\nLower Triangular Matrix:");
        MatrixOpps.printMatrix(lowerTriangle);
    }
}
