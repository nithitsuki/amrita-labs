import java.util.*;
class Employee {
    int empID;
    String name;
    String designation;
    double Salary;

    Employee(int empID, String name, String designation, double Salary) {
        this.empID = empID;
        this.name = name;
        this.designation = designation;
        this.Salary = Salary;
    }
    void display()
    {
        System.out.printf("Name is %s, id is %d, designation is %s, salary is %.2f\n",name,empID,designation,Salary);
    }
} 

public class LAB6_Q7_Emplyee_Management_system {
    // Create a class employee with empID, name, Designtion and salay
    // store 5 emps data
    // i) Display details of employee whose empid is 102
    // ii) display employess whose salary is above 50,000
    public static void main(String[] args) {
        Employee employees[] = { new Employee(100, "Aditi"       , "CEO", 80000),
                                new Employee(101, "Lohit"        , "CEO", 70000),
                                new Employee(102, "Nithil"       , "CEO", 60000),
                                new Employee(103, "Joseph Joestar", "CEO",50000),
                                new Employee(104, "Garry"        , "CEO", 40000) };
        Scanner inpt = new Scanner(System.in);
        System.out.printf("=============\n");
        System.out.printf("1 for employee with id 102: \n");
        System.out.printf("2 for employeees with okay salary: \n");
        System.out.printf("Enter your choice: ");
        int choice = inpt.nextInt();
        System.out.printf("=============\n");
        switch (choice)
        {
            case 1:
                employees[2].display();
                break;
            case 2:
                System.out.printf("Whats a good salary?: ");
                int good_salary = inpt.nextInt();
                for(Employee employee : employees)
                {
                    if (employee.Salary > good_salary) {
                        employee.display();
                    }
                }
                break;
        }
        inpt.close();
    }
}
