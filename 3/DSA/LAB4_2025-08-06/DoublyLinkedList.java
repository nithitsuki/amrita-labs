public class DoublyLinkedList {

    static class Node {
        double data;
        Node next_node;
        Node prev_Node;

        Node(Node prev_Node, double data, Node next_node) {
            this.data = data;
            this.next_node = next_node;
            this.prev_Node = prev_Node;
        }

        Node(double data) {
            this.data = data;
        }
    }

    static void displayAllNodes(Node one) {
        Node head = one;
        while (head.next_node != null) {
            System.out.println("Node " + head.data);
            head = head.next_node;
        }
        System.out.println("Node " + head.data);

    }

    static void AddNodeAfter(double data, Node head, Node newNode) {
        Node temp = head;
        while (temp != null) {
            if (temp.data == data) {
                newNode.next_node = temp.next_node;
                newNode.prev_Node = temp;
                if (temp.next_node != null) {
                    temp.next_node.prev_Node = newNode;
                }
                temp.next_node = newNode;
                break;
            }
            temp = temp.next_node;
        }
    }

    static void AddNodeBefore(double data, Node head, Node newNode) {
        Node temp = head;
        while (temp != null) {
            if (temp.data == data) {
                newNode.prev_Node = temp.prev_Node;
                newNode.next_node = temp;
                if (temp.prev_Node != null) {
                    temp.prev_Node.next_node = newNode;
                }
                temp.prev_Node = newNode;
                break;
            }
            temp = temp.next_node;
        }
    }

    static Node SortNode(Node head) {
        if (head == null){
            return null;}
        boolean swapped;
        do {
            swapped = false;
            Node temp = head;
            while (temp.next_node != null) {
                if (temp.data > temp.next_node.data) {
                    double t = temp.data;
                    temp.data = temp.next_node.data;
                    temp.next_node.data = t;
                    swapped = true;
                }
                temp = temp.next_node;
            }
        } while (swapped);
        return head;
    }

    static void DeleteNodesOfValue(double data, Node head) {
        Node temp = head;
        while (temp != null) {
            if (temp.data == data) {
                if (temp.prev_Node != null) {
                    temp.prev_Node.next_node = temp.next_node;
                }
                if (temp.next_node != null) {
                    temp.next_node.prev_Node = temp.prev_Node;
                }
            }
            temp = temp.next_node;
        }
    }

        
    public static void main(String[] args) {
        Node three = new Node(null, 3, null);
        Node two = new Node(null, 2, three);
        Node one = new Node(null, 1, two);
        two.prev_Node = one;
        three.prev_Node = two;

        System.out.println("----Displaying all the Nodes in the DLL:");
        displayAllNodes(one);

        System.out.println("Q1. Add Node after the target");
        Node TwoPointFive = new Node(null, 2.5, null);
        AddNodeAfter(2, one, TwoPointFive);
        displayAllNodes(one);

        System.out.println("Q2. Add Node before the target");
        Node ZeroPointFive = new Node(null, 0.5, null);
        AddNodeBefore(1, one, ZeroPointFive);
        // Update head if new node is added before the first node
        if (one.prev_Node != null) {
            one = one.prev_Node;
        }
        displayAllNodes(one);

        System.out.println("Q3. Sort nodes using bubble sort:");
        one = SortNode(one);
        displayAllNodes(one);

        System.out.println("Q4. Delete Node of target value 2.5");
        DeleteNodesOfValue(2.5, one);
        displayAllNodes(one);
    }

}