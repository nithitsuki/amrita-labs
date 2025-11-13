import root.Matrices.lib.MatrixOpps;

public class IdentityMatrice {
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        System.out.println("Enter the size of the square matrix:");
        int n = sc.nextInt();
        int[][] matrix = new int[n][n];
        System.out.println("Enter the elements of the matrix:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        boolean isIdentity = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ((i == j && matrix[i][j] != 1) || (i != j && matrix[i][j] != 0)) {
                    isIdentity = false;
                    break;
                }
            }
            if (!isIdentity) break;
        }
        if (isIdentity) {
            System.out.println("The given matrix is an identity matrix.");
        } else {
            System.out.println("The given matrix is not an identity matrix.");
        }
        sc.close();
    }
}