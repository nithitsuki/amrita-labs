package DSA.a.b.c.d;

import java.util.PriorityQueue;
import java.util.Collections;

public class Practice {
    public static void main(String[] args) {
        PriorityQueue<Job> pqMax = new PriorityQueue<Job>();
        Job j1 = new Job(Priority.MEDIUM);
        Job j2 = new Job(Priority.LOW);
        Job j3 = new Job(Priority.NONE);
        Job j4 = new Job(Priority.VERY_HIGH);
        Job j5 = new Job(Priority.HIGH);
        Job j6 = new Job(Priority.VERY_HIGH);

        pqMax.add(j1);
        pqMax.add(j2);
        pqMax.add(j3);
        pqMax.add(j4);
        pqMax.add(j5);
        pqMax.add(j6);



        PriorityQueue<Job> pqMin = new PriorityQueue<Job>(Collections.reverseOrder());
        pqMin.add(j1);
        pqMin.add(j2);
        pqMin.add(j3);
        pqMin.add(j4);
        pqMin.add(j5);
        pqMin.add(j6);

        System.out.println("pqMax (natural order):");
        while (!pqMax.isEmpty()) {
            System.out.println(pqMax.poll());
        }

        System.out.println("pqMin (reverse order):");
        while (!pqMin.isEmpty()) {
            System.out.println(pqMin.poll());
        }
    }

}
