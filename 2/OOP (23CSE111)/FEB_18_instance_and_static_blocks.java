public class FEB_18_instance_and_static_blocks {
    int glbl_var = 10;
    static int glbl_static_var = 10;

    {System.out.println("This is in a instance block before static block");}
    static {System.out.println("This is in a static block before main()");}

    public static void main(String[] args) {
        System.out.printf("This is the main function code\n");
    }

    {System.out.println("This is in a instance block after main()");}
}
