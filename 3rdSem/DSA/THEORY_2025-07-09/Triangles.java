import java.util.*;
import java.util.function.BinaryOperator;

public class Triangles {

  static <T extends Comparable<T>> List<List<T>> PossibleTriangles(T[] arr, BinaryOperator<T> adder) {
    List<List<T>> listOfValidTriangles = new ArrayList<>();
    int num_triangles_found = 0;

    int max = arr.length;

    for (int pointerOne = 0; pointerOne < max - 2; pointerOne++) {
      for (int pointerTwo = pointerOne + 1; pointerTwo < max - 1; pointerTwo++) {
        for (int pointerThree = pointerTwo + 1; pointerThree < max; pointerThree++) {
          T A = arr[pointerOne];
          T B = arr[pointerTwo];
          T C = arr[pointerThree];

          if (adder.apply(A, B).compareTo(C) > 0 && adder.apply(A, C).compareTo(B) > 0
              && adder.apply(B, C).compareTo(A) > 0) {
            listOfValidTriangles.add(Arrays.asList(A, B, C));
            num_triangles_found++;
          }
        }
      }
    }

    return listOfValidTriangles;
  }

  public static void main(String[] args) {
    Integer[] nums = { 4, 6, 3, 7 };
    System.out.println(PossibleTriangles(nums, Integer::sum));
  }

}
