interface TicketBooking {
    void bookTicket();
    void cancelTicket();
}

class FlightBooking implements TicketBooking {
    public void bookTicket() {
        System.out.println("Flight Ticket Booked");
    }
    public void cancelTicket() {
        System.out.println("Flight Ticket Cancelled");
    }
}

class TrainBooking implements TicketBooking {
    public void bookTicket() {
        System.out.println("Train Ticket Booked");
    }
    public void cancelTicket() {
        System.out.println("Train Ticket Cancelled");
    }
}

class ifq8 {
    public static void main(String[] args) {
        TicketBooking flight = new FlightBooking();
        TicketBooking train = new TrainBooking();
        flight.bookTicket();
        flight.cancelTicket();
        train.bookTicket();
        train.cancelTicket();
    }
}