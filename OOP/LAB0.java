import java.util.*;

public class LAB0 {
    public void main(String[] args) {
        Scanner inpt = new Scanner(System.in);
        System.out.print("Enter Your Name: ");
        final String $name = inpt.nextLine();
        System.out.print("Enter your age: ");
        int _age = inpt.nextInt();
        System.out.println("Welcome! "+$name+" Your "+_age+" years old");
        inpt.close();
    }
}
