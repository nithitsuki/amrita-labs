abstract class Mammal
{
    int age;
    int weight;
    String name;
}

class Bird extends Mammal
{
    int no_feathers;
}

class Human extends Mammal{
    int salary;
    //variable = property
    //method = function (python)
    void display(){
        System.out.println("My name is ajay");
    }
    int add(int a, int b){
        return a + b;
    }
    Human(int a, String b)
    {
        // a = 18, b = Lohit
        age = a;
        name = b;
    }
}
public class MAR_6 {
    public static void main(String[] args) {
        Human ramesh = new Human(19,"ramesh");
    }
}
