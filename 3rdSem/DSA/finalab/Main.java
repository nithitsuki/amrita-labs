package finalab;

public class Main {
    static class Graph{
    int v;
    int[][] adj;
    
    Graph(int v){
        this.v = v;
        adj = new int[v][v];
    }
    void addEdge(int src_vertex, int dest_vertex){
        adj[src_vertex][dest_vertex] = 1;
        adj[dest_vertex][src_vertex] = 1;
    }
    class Queue{
        int[] arr;
        int front = 0;
        Queue(int size){
            this.arr = new int[size];
        }
        int rear = -1;
        int size = 0;
        boolean isEmpty() {return (size == 0);}
        void add(int e){
            rear++;
            arr[rear] = e;
            size++;
        }
        int poll(){
            front +=1;
            size -=1;
            return arr[front-1];
        }
    }
    void BFS(){
        Queue q = new Queue(v);
        boolean[] visited = new boolean[v];
        int curr_vertex_row_idx = 0;
        visited[curr_vertex_row_idx] = true;
        System.out.print(curr_vertex_row_idx + " ");
        for (int dest_vertx_idx = 0; dest_vertx_idx < v; dest_vertx_idx++) {
            if(adj[curr_vertex_row_idx][dest_vertx_idx] > 0 && !visited[dest_vertx_idx])
            q.add(dest_vertx_idx);
        }
        while (!q.isEmpty()) {
           curr_vertex_row_idx = q.poll();
           System.out.print(curr_vertex_row_idx + " ");
           visited[curr_vertex_row_idx] = true;
           for(int i = 0; i < v; i++){
                if(adj[curr_vertex_row_idx][i] > 0 && !visited[i]){
                    q.add(i);
                }
           }
    }
   }
   }
   public static void main(String[] args) {
    Graph g = new Graph(6);
    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,3);
    g.addEdge(1,4);
    g.addEdge(2,5);
    g.BFS();
   }
}