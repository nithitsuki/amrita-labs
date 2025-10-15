package com.fone.ftwo;

public class Node{
    Node left = null;
    Node right = null;
    int data;
    Node(int data)
    {this.data = data;}
}

// nov 1 lab eval
// oct last week quiz 2

public class BT {
    Node root;
    BT(Node rootNode)
    {
        root = rootNode;
    }
    Node getRoot(){return root;}
    
    int numberOfLeaves(Node node)
    {   node = (node == null) ? root: node;
        if(node == null) {return 0;}
        if(node.left == null && node.right == null) {return 1;}
        return numberOfLeaves(node.left) + numberOfLeaves(node.right);
    }
}
