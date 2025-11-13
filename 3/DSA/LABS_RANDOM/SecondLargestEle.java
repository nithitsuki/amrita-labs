public class SecondLargestEle {
    static <T extends Comparable<T>> T FindSecondLargest(T[] arr)
    {
        T largestElement = arr[0];
        T SecondLargest = null;
        for(T element: arr)
        {
            if(element.compareTo(largestElement) > 0)
            {SecondLargest = largestElement; largestElement = element;}
            else if ((SecondLargest == null || element.compareTo(SecondLargest) > 0) && element.compareTo(largestElement) != 0)
            {SecondLargest = element;}
        }
        return SecondLargest;
    }

    public static void main(String[] args) 
    {
        Integer[] Arr = {1,2,3};
        for(Integer i: Arr)
        {
            System.out.print(i+",");
        }
        System.err.println();
        System.out.println("Second largest element is: "+FindSecondLargest(Arr));
    }
}
