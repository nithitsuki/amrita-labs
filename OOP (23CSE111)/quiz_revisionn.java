class Student
{
    String name;
}

public class quiz_revisionn {
    public static void main(String[] args) {
        Student bench_of_students[] = new Student[10];
        
        for(Student s : bench_of_students)
        {
            s = new Student();
            s.name = "default name";
        }

        for(int i = 0; i < 10; i++)
        {
            bench_of_students[i] = new Student();
            bench_of_students[i].name = "default name";
        }
    }
}
