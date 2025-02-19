import java.util.*;
public class Feb_5 {
    public static void sum_of_digits(int n)
    {
        int sum_e = 0;
        int sum_o = 0;
        while(n > 0)
        {
            if((n % 10) % 2 == 0){
            sum_e += n % 10;
            }
            else
            {sum_o += n % 10;
            }
            n = n / 10;
        }
        System.out.println("The sum of even digits: "+sum_e);
        System.out.println("The sum of odd digits: "+sum_o);
        System.out.println("The sum of all digits: "+ (sum_o+sum_e));
    }
    public static void main(String[] args){
        Scanner inpt = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = inpt.nextInt();
        sum_of_digits(n);
        inpt.close();
    }
    
}
