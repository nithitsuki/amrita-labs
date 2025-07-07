import java.util.Scanner;

class Student
{
    String Name = "default_name";
    int Marks = 0;
    public void set_details(String name, int marks)
    {
        Name = name;
        Marks =  marks;
    }
    public void print_details()
    {
        System.out.printf("%s got %d marks \n",this.Name,this.Marks);
    }
}


public class Student_Marks {
    public static void main(String[] args)
    {
        Student arr_of_Students[] = new Student[5];
        Scanner inpt = new Scanner(System.in);
        for(int i = 0; i < 5; i++)
        {
            arr_of_Students[i] = new Student();
            System.out.print("Enter Students Name: ");
            String name = inpt.next();
            System.out.print("Enter Students Marks: ");
            int matks = inpt.nextInt();
            arr_of_Students[i].set_details(name, matks);
        }
        inpt.close();
        for(Student student : arr_of_Students)
        {student.print_details();}
    
    }
}
