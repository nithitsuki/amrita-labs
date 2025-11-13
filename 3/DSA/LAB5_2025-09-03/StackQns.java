import java.util.*;

public class StackQns {
    public static void main(String[] args) {
        Stack<Character> brackets = new Stack<Character>();
        Stack<Character> CharStack = new Stack<Character>();
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = sc.nextLine();

        // Q1
        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            if (ch == '{') {
                brackets.push(ch);
            } else if (ch == '}') {
                if (brackets.isEmpty()) {
                    System.out.println("Not balanced");
                    sc.close();
                    return;
                }
                brackets.pop();
            }
            CharStack.push(ch);
        }
        System.out.println("String is " + (brackets.isEmpty() ? "Balanced" : "Not balanced"));

        // Q2
        String Reversed = "";
        @SuppressWarnings("unchecked")
        Stack<Character> CharStackCopy = (Stack<Character>) CharStack.clone();
        while (!CharStackCopy.isEmpty()) {
            Reversed += CharStackCopy.pop();
        }
        System.out.println("Reversed String is " + Reversed);

        Stack<Character> tempCharStack = new Stack<Character>();
        int originalSize = CharStack.size();
        int half = originalSize / 2;
        for (int i = 0; i < half; i++) {
            tempCharStack.push(CharStack.pop()); // save top half to tempChar
        }
        if (originalSize % 2 == 1) {
            CharStack.pop(); // remove middle element of CharStack
        }
        while (!tempCharStack.isEmpty()) {
            CharStack.push(tempCharStack.pop()); 
        }

        // build the resulting string in original left-to-right order
        String MidRemoved = "";
        @SuppressWarnings("unchecked")
        Stack<Character> CharStackCopy2 = (Stack<Character>) CharStack.clone();
        StringBuilder sb = new StringBuilder();
        while (!CharStackCopy2.isEmpty()) {
            sb.append(CharStackCopy2.pop()); // builds reversed order
        }
        MidRemoved = sb.reverse().toString();
        System.err.println("String with middle character removed is " + MidRemoved);
        sc.close();
    }
}
