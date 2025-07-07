import java.util.*;

class Rectangle
{
    double length,width;
    public Rectangle(double length_inpt,double width_inpt)
    {
        length = length_inpt;
        width = width_inpt;
    }

    public double get_area()
    {
        return length*width;
    }
}


public class Rectangle_Class {
    public static void main(String[] args) {
        Scanner inpt = new Scanner(System.in);
            System.out.printf("Enter length of rectangle: ");
            double length = inpt.nextDouble();
            System.out.printf("Enter length of rectangle: ");
            double width = inpt.nextDouble();

        Rectangle R1 = new Rectangle(length, width);
        System.out.printf("Area of your rectangle: %.2f\n",R1.get_area());

        System.out.printf("How many random rectanges do you want to generate?: ");
        int n = inpt.nextInt();
        inpt.close();
        System.out.println("==========================");

        Rectangle arr_of_rects[] = new Rectangle[n];

        Random rand = new Random(); int i = 1;
        for(Rectangle rect : arr_of_rects)
        {
            rect = new Rectangle(rand.nextDouble()*10, rand.nextDouble()*10);
            System.out.printf("Length of rectangle number %d in array: %.2f\n",i,rect.length);
            System.out.printf("Width of rectangle number %d in array: %.2f\n",i,rect.width);
            System.out.printf("Area of rectangle number %d in array: %.2f\n",i,rect.get_area());
            System.out.println("==========================");
            i++;
        }

    }
}