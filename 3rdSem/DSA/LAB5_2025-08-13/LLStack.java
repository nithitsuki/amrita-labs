public class LLStack {
    Node top;
    public int size;
    int maxSize = 100;

    class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            next = null;
        }

        Node(int data, Node next) {
            this.data = data;
            this.next = next;
        }
    }

    LLStack() {
        top = null;
        size = 0;
    }

    boolean isFull() {
        return size == (maxSize);
    }

    boolean isNull() {
        return (size == 0);
    }

    void push(int x) {
        Node n = new Node(x, top);
        top = n;
        size++;
    }

    int pop() {
        int val = top.data;
        top = top.next;
        size--;
        return val;
    }

    int peek() {
        return top.data;
    }

    static void EmptyAndPrint(LLStack currentStack) {
        System.out.println("The stack:");
        while(!currentStack.isNull()){
            System.out.println(currentStack.pop());
        }
    }

    public static void main(String[] args) {
        LLStack MyStack = new LLStack();
        MyStack.push(10);
        MyStack.push(20);
        MyStack.push(30);
        EmptyAndPrint(MyStack);

        System.out.println("Adding 10,20,30 and popping 30");
        MyStack.push(10);
        MyStack.push(20);
        MyStack.push(30);
        MyStack.pop();
        EmptyAndPrint(MyStack);

        System.out.println("Emptying the stack by popping 20 and 10, and checking if emmpty");
        MyStack.push(10);
        MyStack.push(20);
        MyStack.pop();
        MyStack.pop();
        MyStack.pop();
        System.out.println("Is the stack empty?: " + MyStack.isNull());
    }
}
