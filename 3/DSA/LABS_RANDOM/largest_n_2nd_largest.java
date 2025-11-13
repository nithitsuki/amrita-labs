public class largest_n_2nd_largest {
    static <T extends Comparable<T>> T FindLargest(T[] inpt) {
        T Largest = inpt[0];
        for (T element : inpt) {
            if (element.compareTo(Largest) > 0) {
                Largest = element;
            }
        }
        return Largest;
    }

    static <T extends Comparable<T>> T FindSecondLargest(T[] inpt) {
        T Largest = FindLargest(inpt);
        T SecondLargest = null;
        for (T element : inpt) {
            if (element.compareTo(Largest) < 0 && (SecondLargest == null || element.compareTo(SecondLargest) > 0)) {
                SecondLargest = element;
            }
        }
        return SecondLargest;
    }

    static <T extends Comparable<T>> T FindMinimum(T[] arr)
    {
        T Minimum = arr[0];
        for(T element : arr)
        {
            if(element.compareTo(Minimum) < 0)
            {
                Minimum = element;
            }
        }
        return Minimum;
    }
    public static void main(String[] args) {
        Integer[] arr = { 10, 1, 2, 3, 4, 5 };
        Integer Largest = FindLargest(arr);
        System.out.println("Largest is: " + Largest);
        System.out.println("Second Largest is: " + FindSecondLargest(arr));
        System.out.println("Minimum is: " + FindMinimum(arr));
        return;
    }
}
