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

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int caseNum = Integer.parseInt(br.readLine());
		int m, n, k;
		int[][] loca;
		int[][] visit;
		for (int i = 0; i < caseNum; i++) { // 배추 위치 저장
			StringTokenizer st = new StringTokenizer(br.readLine());
			m = Integer.parseInt(st.nextToken()); // 가로
			n = Integer.parseInt(st.nextToken()); // 세로
			k = Integer.parseInt(st.nextToken()); // 배추개수
			loca = new int[n][m];
			visit = new int[n + 2][m + 2];

			for (int j = 0; j < k; j++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				loca[y][x] = 1;
			}

			// BFS나 DFS로 배추 묶여 있는것 찾기

			for (int a = 0; a < m; a++) {
				for (int b = 0; b < n; b++) {
					Queue<Location> q = new LinkedList<>();
					q.offer(new Location(a, b));
				}
			}

		}
	}
}

class Location {
	int x, y;

	public Location(int x, int y) {
		this.x = x;
		this.y = y;
	}
}