public class ReverseLL {

  static class Node {
    String data;
    Node next_node;

    Node(String data, Node next_node) {
      this.data = data;
      this.next_node = next_node;
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

  static Node reverseList(Node head) {
    Node prev = null;
    Node curr = head;
    Node next = null;
    while (curr != null) {
      next = curr.next_node;
      curr.next_node = prev;
      prev = curr;
      curr = next;
    }
    head = prev;
    return head;
  }

  public static void main(String[] args) {
    Node five  = new Node("Node number 5",null);
    Node four  = new Node("Node number 4",         five );
    Node three = new Node("Node number 3",         four );
    Node two   = new Node("Node number 2",         three);
    Node one   = new Node("Node number 1",         two  );

    Node head = one;

    System.out.println("displayAllNodes ");
    displayAllNodes(head);

    System.out.println("Reversed LinkedList");
    head = reverseList(head);
    displayAllNodes(head);
  }
}
