import java.util.Scanner;
public class hello {
    public static void main(String args[])
    {
        Scanner inpt = new Scanner(System.in);
        System.out.print("Enter Size of Triangle: ");
        int n = inpt.nextInt(); 
        for(int i = 0; i < n; i++)
        {
            System.out.println(" ".repeat(n-i)+"*".repeat((2*i)+1));
        }
        inpt.close();
    }
}
