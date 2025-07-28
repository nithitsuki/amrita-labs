public class Feb17_instance_vars {
    /**  Instance Variables: Class Level Scope
    These variables must be declared inside class (outside any function).
    They can be directly accessed anywhere in class.
    */

    // Class Scope variable
    static int glbl_static_var = 11;
  
    // Instance Variable
    private int glbl_var = 33;

    public static void main(String[] args)
    {
        Feb17_instance_vars obj1 = new Feb17_instance_vars();
        System.out.println("unintialzed object glbl_var value: " + obj1.glbl_var);
        System.out.println("glbl_static_var value: " + glbl_static_var);

        glbl_static_var = 3;
        System.out.println("glbl_static_var value after changing: " +glbl_static_var);
    }
}