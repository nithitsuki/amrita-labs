package LAB6;

class Product
{
    String name = "";
    int id = 0;
    Product(int id, String name)
    {
        this.id = id;
        this.name = name;
    }
    void display()
    {
        System.out.printf("Product_ID = %d, Peoduct %s\n",this.id,this.nsame);
    }
}

public class LAB6 {
    public static void main(String[] args) {
        Product[] obj = new Product[5];
        obj[0] = new Product(23907,"Dell Laptop");
        obj[1] = new Product(91240,"HP 360");
        obj[2] = new Product(12323,"LG Oled TV ");
        obj[3] = new Product(23232,"MI Note Pro Max 9");
        obj[4] = new Product(22131,"Kingston USB");
        for(Product p: obj){p.display();}
    }
}