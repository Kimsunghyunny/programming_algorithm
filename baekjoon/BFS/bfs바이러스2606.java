package Main;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

import java.io.IOException;
public class main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int computer = Integer.parseInt(br.readLine()); //컴퓨터수
		int n = Integer.parseInt(br.readLine()); //연결수
		
		boolean[][] connect = new boolean[computer+1][computer+1];
		boolean[] visit = new boolean[computer+1];
		
		for(int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int node1 = Integer.parseInt(st.nextToken());
			int node2 = Integer.parseInt(st.nextToken());
			
			connect[node1][node2] = true;
		}
		
		Queue<Integer> queue = new LinkedList<>();
		
		queue.offer(1);
		visit[1] = true;
		int count = 0;
		
		while(!queue.isEmpty()) {
			int tmp = queue.poll();
			count++;
			
			for(int i=1; i <=computer; i++) {
				if(i != tmp && connect[tmp][i] == true && visit[i] == false) {
				queue.offer(i);
				visit[i] = true;
				}
			}
		}
		System.out.print(--count);
	}
}