public class SortLL {

  static class Node {
    int data;
    Node next_node;

    Node(int data, Node next_node) {
      this.data = data;
      this.next_node = next_node;
    }
  }

  static void displayAllNodes(Node one) {
    Node head = one;
    while (head.next_node != null) {
      System.out.println(head.data);
      head = head.next_node;
    }
    System.out.println(head.data + " links to nowhere");
    System.out.println();
  }

  static int FindNodeCount(Node head) {
    int i = 0;
    while (head != null) {
      i++;
      head = head.next_node;
    }
    return i;
  }

  static Node SortLinkedList(Node head) {
    boolean swapped;
    do {
      swapped = false;
      Node current = head;
      while (current.next_node != null) {
        if (current.data > current.next_node.data) {
          int temp = current.data;
          current.data = current.next_node.data;
          current.next_node.data = temp;
          swapped = true;
        }
        current = current.next_node;
      }
    } while (swapped);
    return head;
  }

  public static void main(String[] args) {
    java.util.Random rand = new java.util.Random();
    Node six = new Node(rand.nextInt(100), null);
    Node five = new Node(rand.nextInt(100), six);
    Node four = new Node(rand.nextInt(100), five);
    Node three = new Node(rand.nextInt(100), four);
    Node two = new Node(rand.nextInt(100), three);
    Node one = new Node(rand.nextInt(100), two);

    Node head = one;

    System.out.println("display All Nodes ");
    displayAllNodes(head);

    System.out.println("Sorted Linked List: ");
    head = SortLinkedList(head);
    displayAllNodes(head);

  }
}
