abstract class Prod {
    String name;
    double price;

    Prod(String n, double p) {
        name = n;
        price = p;
    }

    abstract void display();
}

interface Disc {
    void applyDisc();
}

class Elec extends Prod implements Disc {
    Elec(String n, double p) {
        super(n, p);
    }

    public void applyDisc() {
        price *= 0.9; // 10% discount
    }

    void display() {
        System.out.println("Elec: " + name + ", Price: $" + price);
    }
}

class Cloth extends Prod implements Disc {
    Cloth(String n, double p) {
        super(n, p);
    }

    public void applyDisc() {
        price *= 0.8; // 20% discount
    }

    void display() {
        System.out.println("Cloth: " + name + ", Price: $" + price);
    }
}

class Shoprcart {
    Prod[] items = new Prod[10];
    int count = 0;

    void addItem(Prod item) {
        if (count < items.length) {
            items[count++] = item;
        } else {
            System.out.println("Cart is full!");
        }
    }

    void applyAllDiscs() {
        for (int i = 0; i < count; i++) {
            if (items[i] instanceof Disc) {
                ((Disc) items[i]).applyDisc();
            }
        }
    }

    void displayCart() {
        for (int i = 0; i < count; i++) {
            items[i].display();
        }
    }
}

class q9 {
    public static void main(String[] args) {
        Shoprcart cart = new Shoprcart();

        Prod phone = new Elec("Smartphone", 500);
        Prod shirt = new Cloth("T-Shirt", 50);
        Prod laptop = new Elec("Laptop", 1000);

        cart.addItem(phone);
        cart.addItem(shirt);
        cart.addItem(laptop);

        System.out.println("Before Discounts:");
        cart.displayCart();

        cart.applyAllDiscs();

        System.out.println("\nAfter Discounts:");
        cart.displayCart();
    }
}