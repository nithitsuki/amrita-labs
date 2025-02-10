import java.util.*;

class Question_ans
{
    static int ask_int_input(Scanner inpt){
        System.out.printf("Enter the number: ");
        int a = inpt.nextInt();
        return a;
    }
    static String question_1 = "Q1. Check wether number is positive or negative\n";
    static String question_2 = "Q2. Check wether number is positive or negative or zero\n";
    static String question_3 = "Q3. Sum of even and odd digits in number\n";
    static String question_4 = "Q4. Check whether person is eligible for voting\n";
    static String question_5 = "Q5. Find the largest of 3 numbers\n";
    static String question_6 = "Q6. Check Grade of your Score\n";
    static String question_7 = "Q7. Grade a String, 5 points for a vowel, 10 for number, 0 for rest\n";
    static String question_8 = "Q8. print case of string, if  upper, lower or mixed\n";
    static String question_9 = "Q9. find discrimant and type of root\n";
    static String question_10= "Q10.\n";

    static void ans_1(int a)
    {
        if(a > 0)
            {System.out.printf("This is a positive number\n");}
        else
            {System.out.printf("This is a negative number\n");}
    }
    static void ans_2(int a)
    {
        if(a > 0)
            {System.out.printf("This is a positive number\n");}
        else if (a < 0)
            {System.out.printf("This is a negative number\n");}
        else
            {System.out.printf("This is a zero number\n");}
    }
    static void ans_3(int a)
    {
        int[] sum = {0,0};
        while(a > 0)
        {
            if((a % 10) % 2 == 0)
            {sum[0] += (a % 10);}
            else{sum[1] += (a % 10);}
            a /= 10;
        }
        System.out.printf("sum of odd digits: %d\nsum of even digits: %d\n",sum[1],sum[0]);
    }
    static void ans_4(int age)
    {
        if(age >= 18)
            {System.out.printf("This person is eligible to vote\n");}
        else
            {System.out.printf("This person is NOT eligible to vote\n");}
    }
    static void ans_5(int a, int b, int c)
    {
        System.out.printf("Largest number is ");
        if((a >= b) && (a >= c))
        {System.out.printf("%d\n",a);}
        else if ((b >= a) && (b >= c))
        {System.out.printf("%d\n",b);}
        else
        {System.out.printf("%d\n",c);}
    }
    static void ans_6(int a)
    {
        System.out.printf("Your Grade is: ");
        if(a >= 80)
        {System.out.printf("A\n");}
        else if(a >= 60)
        {System.out.printf("B\n");}
        else if(a >= 60)
        {System.out.printf("C\n");}
        else if(a >= 40)
        {System.out.printf("B\n");}
        else
        {System.out.printf("F\n");}

    }
    static void ans_7(String a){
        // vowel - 5
        // number - 10
        // 0 for other
        int sum = 0;
        for(int i = 0; i < a.length(); i++)
        {
            if((a.charAt(i) >= '0' ) && (a.charAt(i) <= '9' ) )
            {sum += 10;}
            else if( (a.charAt(i) == 'a' ) || (a.charAt(i) == 'e' ) ||(a.charAt(i) == 'i' ) ||(a.charAt(i) == 'o' ) ||(a.charAt(i) == 'u' ))
            {sum += 10;}
            else if( (a.charAt(i) == 'A' ) || (a.charAt(i) == 'E' ) ||(a.charAt(i) == 'I' ) ||(a.charAt(i) == 'O' ) ||(a.charAt(i) == 'U' ))
            {sum += 10;}
            else
            {sum += 0;}
        }
        System.out.printf("Final value of word is: %d\n",sum);
    }
    static void ans_8(String a){
     boolean has_upper = false;
     boolean has_lower = false;
     for(int i = 0; i < a.length(); i ++)
     {
        if(Character.isLowerCase(a.charAt(i)))
        {has_lower = true;}
        else if(Character.isUpperCase(a.charAt(i)))
        {has_upper = true;}
     }
     if(has_lower && !has_upper)
     {System.out.println("This is lower case word");}
     else if(has_lower && !has_upper)
     {System.out.println("This is lower case word");}
    }}

public class LAB3 {
    public static void main(String[] args) {
        int a,b,c = 0;
        Scanner inpt = new Scanner(System.in);
        // System.out.printf("==================\n");
        // System.out.printf(Question_ans.question_1);
        // a = Question_ans.ask_int_input(inpt);
        // Question_ans.ans_1(a);

        // System.out.printf("==================\n");
        // System.out.printf(Question_ans.question_2);
        // a = Question_ans.ask_int_input(inpt);
        // Question_ans.ans_2(a);

        // System.out.printf("==================\n");
        // System.out.printf(Question_ans.question_3);
        // a = Question_ans.ask_int_input(inpt);
        // Question_ans.ans_3(a);

        // System.out.printf("==================\n");
        // System.out.printf(Question_ans.question_4);
        // a = Question_ans.ask_int_input(inpt);
        // Question_ans.ans_4(a);

        // System.out.printf("==================\n");
        // System.out.printf(Question_ans.question_5);
        // a = Question_ans.ask_int_input(inpt);
        // b = Question_ans.ask_int_input(inpt);
        // c = Question_ans.ask_int_input(inpt);
        // Question_ans.ans_5(a,b,c);

        // System.out.printf("==================\n");
        // System.out.printf(Question_ans.question_6);
        // a = Question_ans.ask_int_input(inpt);
        // Question_ans.ans_6(a);

        // System.out.printf("==================\n");
        // System.out.printf(Question_ans.question_7);
        // System.out.printf("Enter your word: ");
        // String s = inpt.nextLine();
        // Question_ans.ans_7(s);

        System.out.printf("==================\n");
        System.out.printf(Question_ans.question_8);
        System.out.printf("Enter your word: ");
        String s = inpt.nextLine();
        Question_ans.ans_8(s);

        // System.out.printf("==================\n");
        // System.out.printf(Question_ans.question_9);
        // a = Question_ans.ask_int_input(inpt);
        // b = Question_ans.ask_int_input(inpt);
        // c = Question_ans.ask_int_input(inpt);
        // Question_ans.ans_9(a,b,c)

        System.out.printf("==================\n");
        inpt.close();   
    }
}
