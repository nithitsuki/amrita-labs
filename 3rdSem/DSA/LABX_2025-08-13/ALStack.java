import java.util.ArrayList;

public class ALStack {
    private ArrayList<Integer> hiii = new ArrayList<Integer>(); // done?
    private Integer size = 0;
    public void push(Integer x)
    {
        hiii.add(x);
    }

    public Integer pop()
    {
        return hiii.get(size--);
    }
    public static void main(String[] args) {

        hiii.add(10);
        hiii.add(20);
        hiii.add(30);

    }
}