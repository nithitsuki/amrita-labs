public class LinkedListAssignment {

  static class Node {
    String data;
    Node next_node;

    Node(String data, Node next_node) {
      this.data = data;
      this.next_node = next_node;
    }

    Node(String data) {
      this.data = data;
    }
  }

  static void displayAllNodes(Node one) {
    Node head = one;
    while (head.next_node != null) {
      System.out.println(head.data + " links to " + head.next_node.data);
      head = head.next_node;
    }
    System.out.println(head.data + " links to nowhere");
  }

  static void InsertNodeAtSart(Node newHead, Node head) {
    newHead.next_node = head;
  }

  static Node GetTailNode(Node head) {
    while (head.next_node != null) {
      head = head.next_node;
    }
    return head;
  }

  static void InsertNodeAtEnd(Node newTail, Node head) {
    newTail.next_node = null;
    Node oldTail = GetTailNode(head);
    oldTail.next_node = newTail;
  }

  static void DeleteTailNode(Node head) {
    Node temp = head;
    while (temp.next_node.next_node != null) {
      temp = temp.next_node;
    }
    temp.next_node = null;
  }

  static void GetNodeIndex(Node head, String data) {
    int i = 0;
    while (head != null) {
      i++;
      if (head.data == data) {
        System.out.println("Found data at position: " + i);
        return;
      }
      head = head.next_node;
    }
  }

  static void PrintNodeCount(Node head) {
    int i = 0;
    while (head != null) {
      i++;
      head = head.next_node;
    }
    System.out.println("There are " + i + " nodes");
  }

  public static void main(String[] args) {
    Node five = new Node("Node number 5", null);
    Node four = new Node("Node number 4", five);
    Node three = new Node("Node number 3", four);
    Node two = new Node("Node number 2", three);
    Node one = new Node("Node number 1", two);

    Node head = one;

    System.out.println("--Q1: displayAllNodes ");
    displayAllNodes(head);

    System.out.println("--Q2.1: Adding node to start ");
    Node zero = new Node("Node number 0", null);
    InsertNodeAtSart(zero, head);
    head = zero;
    displayAllNodes(head);

    System.out.println("--Q2.2: Adding node to the end");
    Node six = new Node("Node number 6", null);
    InsertNodeAtEnd(six, head);
    displayAllNodes(head);

    System.out.println("--Q3.1: Deleting node at the start");
    head = head.next_node;
    displayAllNodes(head);

    System.out.println("--Q3.2: Deleting node at the End");
    DeleteTailNode(head);
    displayAllNodes(head);

    System.out.println("--Q4: Finding Index of Node with data \"Node number 3\" ");
    GetNodeIndex(head, "Node number 3");

    System.out.println("--Q5: Count the total number of nodes");
    PrintNodeCount(head);
  }
}
