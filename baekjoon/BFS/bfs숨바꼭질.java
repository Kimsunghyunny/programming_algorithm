package Main;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.LinkedList;

class main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int x = Integer.parseInt(st.nextToken());
		int y = Integer.parseInt(st.nextToken());
		
		bfs(x,y);
	}
	
	public static void bfs(int x, int y) {
		Queue<Integer> q = new LinkedList<>();
		q.offer(x);
		
		int[] visit = new int[100002];
		visit[x] = 0;
		
		while(!q.isEmpty()) {
			int tmp = q.poll();
			
			if(tmp==y) break;
			
			if(tmp+1<10001 && visit[tmp+1] == 0) {
				q.offer(tmp+1);
				visit[tmp+1] = visit[tmp]+1;
			}
			if(tmp-1>-1 && visit[tmp-1] == 0) {
				q.offer(tmp-1);
				visit[tmp-1] = visit[tmp]+1;
			}
			if(2*tmp<10001 && visit[2*tmp] == 0) {
				q.offer(2*tmp);
				visit[2*tmp] = visit[tmp]+1;
			}
		}
		System.out.print(visit[y]);
	}
}