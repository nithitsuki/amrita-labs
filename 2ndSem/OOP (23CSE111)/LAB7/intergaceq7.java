interface SmartDevice {
    void turnOn();
    void turnOff();
}

class SmartBulb implements SmartDevice {
    public void turnOn() {
        System.out.println("Smart Bulb Turned On");
    }
    public void turnOff() {
        System.out.println("Smart Bulb Turned Off");
    }
    public void changeColor(String color) {
        System.out.println("Smart Bulb Color Changed to " + color);
    }
}

class SmartAC implements SmartDevice {
    public void turnOn() {
        System.out.println("Smart AC Turned On");
    }
    public void turnOff() {
        System.out.println("Smart AC Turned Off");
    }
    public void setTemperature(int temp) {
        System.out.println("Smart AC Temperature Set to " + temp + "°C");
    }
}

class intergaceq7 {
    public static void main(String[] args) {
        SmartDevice bulb = new SmartBulb();
        SmartDevice ac = new SmartAC();
        bulb.turnOn();
        ((SmartBulb) bulb).changeColor("Blue");
        bulb.turnOff();
        ac.turnOn();
        ((SmartAC) ac).setTemperature(22);
        ac.turnOff();
    }
}