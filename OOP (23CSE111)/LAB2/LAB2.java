// Problem statement: Create functions for 7 questions
// extra diffuculty: use classes
//codename: Classes and Functions

import java.util.*;

class MYMATH{
    public static double add_2_nos(double a, double b) {
        return a + b;
    }

    public static double add_3_nos(double a, double b, double c) {
        return a + b + c;
    }

    public static double area_of_sqr(double a) {
        return a * a;
    }

    public static double area_of_rect(double a, double b) {
        return a * b;
    }

    public static double area_of_circle(double r) {
        return (3.14 * r * r);
    }

    public static double find_disc(double a, double b, double c) {
        return (b * b) - (2 * a * c);
    }

    public static double find_sqrt(double a) {
        double x = Math.sqrt(a);
        return x;
    }

}

public class LAB2 {
    public static void main(String[] args)
    {
        Scanner inpt = new Scanner(System.in);
        System.out.print("Enter Your First Number (a): ");
        double a = inpt.nextDouble();
        System.out.print("Enter Your Second Number (b): ");
        double b = inpt.nextDouble();
        System.out.print("Enter Your Third Number (c): ");
        double c = inpt.nextDouble();
        //Question 1
        System.out.println("Sum of 2 numbers: " + MYMATH.add_2_nos(a, b));
        //Question 2
        System.out.println("Sum of 3 numbers: " + MYMATH.add_3_nos(a, b, c));
        //Question 3
        System.out.println("Area of Square (a): " + MYMATH.area_of_sqr(a));
        //Question 4
        System.out.println("Area of rectangle: (a*b)" + MYMATH.area_of_rect(a, b));
        //Question 5
        System.out.println("Area of circle: (radius=a)" + MYMATH.area_of_circle(a));
        //Question 6
        System.out.println("Discriminant: " + MYMATH.find_disc(a, b, c));
        //Question 7
        System.out.println("Squareroot of first number (a): " + MYMATH.find_sqrt(a));
        inpt.close();
    }
}
