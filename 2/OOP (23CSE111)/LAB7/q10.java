abstract class Veh {
    String model;
    double rentPerDay;

    Veh(String m, double r) {
        model = m;
        rentPerDay = r;
    }

    abstract void display();
}

interface Rentable {
    double calcRent(int days);
}

class Car extends Veh implements Rentable {
    double insuranceCharge;

    Car(String m, double r, double ins) {
        super(m, r);
        insuranceCharge = ins;
    }

    public double calcRent(int days) {
        return (rentPerDay * days) + insuranceCharge;
    }

    void display() {
        System.out.println("Car: " + model + ", Rent/Day: $" + rentPerDay + ", Insurance: $" + insuranceCharge);
    }
}

class Bike extends Veh implements Rentable {
    double helmetDeposit;

    Bike(String m, double r, double dep) {
        super(m, r);
        helmetDeposit = dep;
    }

    public double calcRent(int days) {
        return (rentPerDay * days) + helmetDeposit;
    }

    void display() {
        System.out.println("Bike: " + model + ", Rent/Day: $" + rentPerDay + ", Helmet Deposit: $" + helmetDeposit);
    }
}

class RentSys {
    Veh[] vehicles = new Veh[10];
    int count = 0;

    void addVeh(Veh v) {
        if (count < vehicles.length) {
            vehicles[count++] = v;
        } else {
            System.out.println("Rental system is full!");
        }
    }

    void testRentals(int[] days) {
        for (int i = 0; i < count; i++) {
            vehicles[i].display();
            if (vehicles[i] instanceof Rentable) {
                double total = ((Rentable) vehicles[i]).calcRent(days[i]);
                System.out.println("Total Rent for " + days[i] + " days: $" + total);
            }
            System.out.println();
        }
    }
}

class q10 {
    public static void main(String[] args) {
        RentSys sys = new RentSys();

        Veh car1 = new Car("Toyota Camry", 50, 20);
        Veh bike1 = new Bike("Honda CBR", 20, 10);
        Veh car2 = new Car("Tesla Model S", 100, 30);

        sys.addVeh(car1);
        sys.addVeh(bike1);
        sys.addVeh(car2);

        int[] rentalDays = {3, 5, 2}; // Days for each vehicle

        System.out.println("Rental Details:");
        sys.testRentals(rentalDays);
    }
}