import java.util.Scanner;
import java.math.*;

public class LAB1{
    public static void main(String[] args)
    {
        Scanner inpt = new Scanner(System.in);
        System.out.print("Enter your weight (in kgs): ");
        float weight = inpt.nextFloat();
        System.out.println();
        System.out.print("Enter your hreight (in cm): ");
        float height = inpt.nextFloat();
        System.out.println();
        inpt.close();
        double BMI = weight/(Math.pow((height/100),2));
        System.out.println("YOUR BMI IS "+BMI);
        return;
    }
}
