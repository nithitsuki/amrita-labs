import java.util.Scanner;

class my_funcs {
    
    static boolean check_if_prime(int n)
    {
        boolean is_prime = true;
        for (int i = 2; i < n; i++)
        {
            if (n % i == 0){is_prime = false;break;}
        }
        return is_prime;
    }

}

public class Feb10_prime_numbers {
    public static void main(String args[]) {
        Scanner inpt = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = inpt.nextInt();
        if (my_funcs.check_if_prime(n)){System.out.printf("%d is a prime number\n", n);}
        else {System.out.printf("%d is NOT a prime number\n", n);}
        
        inpt.close();
    }

}
