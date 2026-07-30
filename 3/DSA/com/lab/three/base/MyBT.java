package base;
import java.util.ArrayDeque;;

public class MyBT {
    Node root;
    MyBT(Node root){
        this.root = root;
    }
    void PreOrder(){
        PreOrder(this.root);
    }
    void PreOrder(Node node){
        if(node == null){return;}
        System.out.printf("%d",node.data);
        PreOrder(node.left);
        PreOrder(node.right);
    }
     void InOrder(){
        InOrder(this.root);
     }
     void PostOrder(){
        PostOrder(this.root);
     }
     void InOrder(Node node){
        if(node == null){return;}
        InOrder(node.left);
        System.out.printf("%d",node.data);
        InOrder(node.right);
     }
     void PostOrder(Node node){
        if(node == null){return;}
        PostOrder(node.left);
        PostOrder(node.right);
        System.out.printf("%d",node.data);
     }
     void BFT()
     {
        ArrayDeque<Node> q = new ArrayDeque<Node>();
        q.add(this.root);
        while (!q.isEmpty()) {
        Node cur = (Node)q.pop();
        System.out.printf("%d ",cur.data);
        if(cur.left != null){q.add(cur.left);}
        if(cur.right != null) {q.add(cur.right);}
        }

     }
}