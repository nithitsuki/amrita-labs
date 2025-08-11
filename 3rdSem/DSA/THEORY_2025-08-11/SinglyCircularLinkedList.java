public class SinglyCircularLinkedList {
    private static class Node {
        int data;
        Node next;
        Node(int data) { this.data = data; }
    }

    private Node tail;
    private int size;

    public void insertAtStart(int data) {
        Node node = new Node(data);
        if (tail == null) {
            tail = node;
            node.next = node;
        } else {
            node.next = tail.next;
            tail.next = node;
        }
        size++;
    }

    public void insertAtEnd(int data) {
        insertAtStart(data);
        tail = tail.next;
    }

    public Integer deleteAtStart() {
        if (tail == null) return null;
        Node head = tail.next;
        int val = head.data;
        if (head == tail) {
            tail = null;
        } else {
            tail.next = head.next;
        }
        size--;
        return val;
    }

    public Integer deleteAtEnd() {
        if (tail == null) return null;
        Node head = tail.next;
        if (head == tail) {
            int val = tail.data;
            tail = null;
            size--;
            return val;
        }
        Node current = head;
        while (current.next != tail) {
            current = current.next;
        }
        int val = tail.data;
        current.next = tail.next;
        tail = current;
        size--;
        return val;
    }

    public boolean deleteValue(int value) {
        if (tail == null) return false;
        Node prev = tail;
        Node curr = tail.next;
        do {
            if (curr.data == value) {
                if (curr == tail) {
                    if (curr == tail.next) {
                        tail = null;
                    } else {
                        prev.next = curr.next;
                        tail = prev;
                    }
                } else {
                    prev.next = curr.next;
                }
                size--;
                return true;
            }
            prev = curr;
            curr = curr.next;
        } while (curr != tail.next);
        return false;
    }

    public void display() {
        if (tail == null) {
            System.out.println("List is empty");
            return;
        }
        Node head = tail.next;
        Node current = head;
        StringBuilder sb = new StringBuilder();
        do {
            sb.append(current.data).append(" -> ");
            current = current.next;
        } while (current != head);
        sb.append("(back to head)");
        System.out.println(sb.toString());
    }

    public int size() { return size; }

    // Main function to demonstrate usage
    public static void main(String[] args) {
        SinglyCircularLinkedList list = new SinglyCircularLinkedList();

        System.out.println("Inserting at end: 10, 20, 30");
        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.display();

        System.out.println("Inserting at start: 5");
        list.insertAtStart(5);
        list.display();

        System.out.println("Deleting at start: " + list.deleteAtStart());
        list.display();

        System.out.println("Deleting at end: " + list.deleteAtEnd());
        list.display();

        System.out.println("Deleting value 20: " + list.deleteValue(20));
        list.display();

        System.out.println("Deleting value 100 (not present): " + list.deleteValue(100));
        list.display();

        System.out.println("Current size: " + list.size());
    }
}
