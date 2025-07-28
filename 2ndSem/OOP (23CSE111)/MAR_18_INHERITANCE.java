class Transport 
{
	int speed;
	double accel;
	int capcity;
	int weight;
	String region;
	void display()
	{
		System.out.println("Speed: " + speed);
		System.out.println("accel: " + accel);
		System.out.println("capcity: " + capcity);
		System.out.println("region: " + region);
	}
}
class Car extends Transport
{
	int no_wheels;
	String engine_name;
    @Override
	void display()
	{
		System.out.println("Speed: " + speed);
		System.out.println("accel: " + accel);
		System.out.println("capcity: " + capcity);
		System.out.println("region: " + region);
		System.out.println("no_wheels: " + no_wheels);
		System.out.println("engine_name: " + engine_name);
	}
}

public class MAR_18_INHERITANCE {
	public static void main(String args[])
	{
		Car reveolto = new Car();
		reveolto.speed = 350;
		reveolto.accel = 2.6;
		reveolto.capcity = 2;
		reveolto.weight = 100;
		reveolto.region = "Italy";
		reveolto.no_wheels = 4;
		reveolto.engine_name = "V12";
		reveolto.display();
	}
}
