interface Payment {
    void processPayment(double amt);
    void generateReceipt();
}

class CreditCardPayment implements Payment {
    public void processPayment(double amt) {
        System.out.println("Processing Credit Card Payment: $" + amt);
    }
    public void generateReceipt() {
        System.out.println("Credit Card Receipt Generated");
    }
}

class UPIPayment implements Payment {
    public void processPayment(double amt) {
        System.out.println("Processing UPI Payment: $" + amt);
    }
    public void generateReceipt() {
        System.out.println("UPI Receipt Generated");
    }
}

class intergaceq6 {
    public static void main(String[] args) {
        Payment p1 = new CreditCardPayment();
        Payment p2 = new UPIPayment();
        p1.processPayment(100);
        p1.generateReceipt();
        p2.processPayment(50);
        p2.generateReceipt();
    }
}