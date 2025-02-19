public class FEB_19_constructors {
    int glbl_var = 10;
    static int glbl_static_var = 10;

    // constructor value setter
    FEB_19_constructors(int a, int b) {
        this.glbl_var = a;
        glbl_static_var = b;
    }

    // empty constructor
    FEB_19_constructors() {}

    public static void main(String[] args) {
        FEB_19_constructors obj1 = new FEB_19_constructors();
        System.out.println("unintialzed object glbl_var value: " + obj1.glbl_var);
        System.out.println("glbl_static_var value: " + glbl_static_var);

        FEB_19_constructors obj2 = new FEB_19_constructors(12,34);
        System.out.println("intialzed object glbl_var value: " + obj2.glbl_var);
        System.out.println("glbl_static_var value after intialisation: " + glbl_static_var);
        
        glbl_static_var = 3;
        System.out.println("glbl_static_var value after changing: " +glbl_static_var);
    }
}
