package DSA.a.b.c.d;

import java.io.Serializable;
import java.util.UUID;

enum Priority {
    VERY_HIGH, HIGH, MEDIUM, LOW, NONE
};

public class Job implements Comparable<Job>, Serializable {
    UUID Id = null;
    Priority priority;

    Job(Priority priority) {
        this.priority = priority;
        this.Id = UUID.randomUUID();
    }

    public int compareTo(Job arg0) {
        return this.priority.compareTo(arg0.priority);
    }
    @Override
    public String toString() {
        return this.priority.toString();
    }

}
