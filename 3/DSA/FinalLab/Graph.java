package FinalLab;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Graph<V,E> {
    ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
    int v, e = 0; //no. vertices and edges

    ArrayList<ArrayList<Integer>> Initialize(int v, int[][] e){
        this.v = v;
         for (int i = 0; i < v; i++)
            adj.add(new ArrayList<>());
        for (int[] vertex_edges : e) {
            //vertex edges in the format {u,v}
            // where u<->v. Therefore u->v && v->u
            adj.get(vertex_edges[0]).add(vertex_edges[1]); // u->v
            adj.get(vertex_edges[1]).add(vertex_edges[0]); //v->u
        }
        return adj;
    }
    
    public void DFS(){
        Stack<Integer> s = new Stack<>();
        boolean[] visited = new boolean[v];
        int start = 0;
        visited[start] = true;
        s.push(start);
        while (!s.isEmpty()) {
            int curr = s.pop();
            System.out.print(curr + " ");
            for (int children : adj.get(curr).reversed()) {
                if(!visited[children])
                    s.push(children);
                    visited[children] = true;
            }
        }
    }

    public void BFS(){
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[v];
        int start = 0;
        visited[start] = true;
        q.add(start);
        while (!q.isEmpty()) {
            int curr = q.poll();
            System.out.print(curr + " ");
            for (int children : adj.get(curr)) {
                if(!visited[children])
                    q.add(children);
                    visited[children] = true;
            }
        }
    }

    public static void main(String[] args) {
        Graph<Integer,Integer> g = new Graph<>();
        int v = 6;
        int[][] e = {
            {0,1}, // 0 is connected to 1
            {0,2},
            {1,3},
            {1,4},
            {2,5}
        };
        ArrayList<ArrayList<Integer>> relations = g.Initialize(v,e);
        for (ArrayList<Integer> relation : relations) {
            System.out.println(relation.toString());;
        }
        g.BFS();
        System.out.println();
        g.DFS();
    }
}