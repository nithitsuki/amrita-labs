public class FindMiddleNodeLL {

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

  static Node FindMiddleNode(Node head) {
    Node slow = head;
    Node fast = head;
    Node next;
    while (fast != null && fast.next_node !=null) {
      slow = slow.next_node;
      fast = fast.next_node.next_node;
    }
    return (slow != null) ? slow : null;
  }

  public static void main(String[] args) {
    Node six  = new Node("Node number 6",null);
    Node five  = new Node("Node number 5",         six  );
    Node four  = new Node("Node number 4",         five );
    Node three = new Node("Node number 3",         four );
    Node two   = new Node("Node number 2",         three);
    Node one   = new Node("Node number 1",         two  );

    Node head = one;

    System.out.println("display All Nodes ");
    displayAllNodes(head);

    System.out.println();

    System.out.println("Middle Element: ");
    System.out.println(FindMiddleNode(head).data);
  }
}
