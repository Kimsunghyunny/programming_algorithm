package Main;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Collections;

import java.util.regex.Pattern;

public class main {

	static int m;
	static int n;

	public static void main(String[] args) throws IOException {
		// 시작점이 여러개인 bfs 구현

		int[][] map = new int[1002][1002];
		int[][] count = new int[1002][1002];

		int[] dx = { 0, 1, 0, -1 };
		int[] dy = { 1, 0, -1, 0 };

		Queue<Location> q = new LinkedList<>();

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		m = Integer.parseInt(st.nextToken()); // 가로
		n = Integer.parseInt(st.nextToken()); // 세로

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 1)
					q.offer(new Location(i, j));
				if (map[i][j] == 0)
					count[i][j] = -1;
			}
		}

		while (!q.isEmpty()) {
			Location loc = q.poll();
			for (int i = 0; i < 4; i++) {
				int tmpX = loc.row + dx[i];
				int tmpY = loc.col + dy[i];

				if (checkMap(tmpX, tmpY)) {
					if(count[tmpX][tmpY] >= 0) {
						count[tmpX][tmpY] = count[loc.row][loc.col]+1;
						q.offer(new Location(tmpX, tmpY));
					}
				}
			}
		}
		
		int result = 0;
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(count[i][j] == -1)
					System.out.print("-1");
				result = Math.max(result, count[i][j]);
			}
		}
		
		System.out.print(result);
	}

	public static boolean checkMap(int x, int y) {

		if (x < 0 || y < 0 || x >= m || y >= n)
			return false;
		else
			return true;
	}
}

class Location {
	int row;
	int col;

	public Location(int row, int col) {
		this.row = row;
		this.col = col;
	}
}