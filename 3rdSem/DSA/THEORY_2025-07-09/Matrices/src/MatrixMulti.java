import lib.MatrixOpps;

public class MatrixMulti {
        public static void main(String[] args) {
                java.util.Scanner sc = new java.util.Scanner(System.in);

                System.out.println("Enter elements of first 3x3 matrix:");
                int[][] a = MatrixOpps.getMatrix(sc);

                System.out.println("Enter elements of second 3x3 matrix:");
                int[][] b = MatrixOpps.getMatrix(sc);

                int[][] c = new int[3][3];

                for (int i = 0; i < 3; i++) {
                        for (int j = 0; j < 3; j++) {
                                c[i][j] = 0;
                                for (int k = 0; k < 3; k++) {
                                        c[i][j] += a[i][k] * b[k][j];
                                }
                        }
                }

                System.out.println("Multiplication of two matrices:");
                MatrixOpps.printMatrix(c);
                sc.close();
        }
}
