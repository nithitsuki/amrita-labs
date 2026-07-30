package base;

public class main {
    public static void main(String[] args) {
        Node[] nodeArray = new Node[15]; 
        for (int i = 0; i < 15; i++) {
            nodeArray[i] = new Node(i);
        }
        MyBT tree = new MyBT(nodeArray[0]);
        tree.root.left = nodeArray[1];
        tree.root.right = nodeArray[2];
        nodeArray[1].left = nodeArray[3];
        nodeArray[1].right = nodeArray[4];
        nodeArray[2].left = nodeArray[5];
        nodeArray[2].right = nodeArray[6];
        nodeArray[3].left = nodeArray[7];
        nodeArray[3].right = nodeArray[8];
        nodeArray[4].left = nodeArray[9];
        nodeArray[4].right = nodeArray[10];
        nodeArray[5].left = nodeArray[11];
        nodeArray[5].right = nodeArray[12];

        tree.BFT();
    }
}
