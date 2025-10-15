class Node{
    Node left = null;
    Node right = null;
    int data;
    Node(int data)
    {this.data = data;}
}

// nov 1 lab eval
// oct last week quiz 2

class BT {
    Node root;
    BT(Node rootNode)
    {
        root = rootNode;
    }
    Node getRoot(){return root;}
    
    int numberOfLeaves(Node node)
    {
        if(node == null) {return 0;}
        if(node.left == null && node.right == null) {return 1;}
        return numberOfLeaves(node.left) + numberOfLeaves(node.right);
    }

    int numberOfNodes(Node root)
    {
        if(root == null) {return 0;}
        return 1 + numberOfNodes(root.left) + numberOfNodes(root.right);
    }

    int numberOfInternalNodes(Node root)
    {
        if(root == null || (root.left == null && root.right == null)) {return 0;}
        return 1 + numberOfInternalNodes(root.left) + numberOfInternalNodes(root.right);
    }

    void PreOrder(Node node)
    {
        if (node == null) return;
        System.out.print(node.data + " ");
        PreOrder(node.left);
        PreOrder(node.right);
    }

    static void InOrder(Node node)
    {
        if (node == null) return;
        InOrder(node.left);
        System.out.print(node.data + " ");
        InOrder(node.right);
    }

    static void PostOrder(Node node)
    {
        if (node == null) return;
        PostOrder(node.left);
        PostOrder(node.right);
        System.out.print(node.data + " ");
    }

}

public class test {
    public static void main(String[] args) {
        // Create nodes for the binary tree
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        
        BT binaryTree = new BT(root);
        
        System.out.println("Number of leaf nodes: " + binaryTree.numberOfLeaves(binaryTree.getRoot()));
        System.out.println("Number of nodes: " + binaryTree.numberOfNodes(binaryTree.getRoot()));

        BT.PostOrder(binaryTree.getRoot());
        System.err.println("");
        BT.InOrder(binaryTree.getRoot());
    }

}
