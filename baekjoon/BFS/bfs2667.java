package Main;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Queue;
import java.util.Arrays;
import java.util.LinkedList;

class Location {
	int row, col;

	public Location(int row, int col) {
		this.row = row;
		this.col = col;
	}
}

public class bfs2667 {

	static int n;
	static int[][] arr;
	static boolean[][] visit;
	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// 단지번호 붙이기 --> 시작점이 여러개인 bfs를 통해 해결해보자.
		// 집의 개수를 가진 개수 배열은 counting을 이용해서 해결하자.
		n = Integer.parseInt(br.readLine());
		arr = new int[n + 2][n + 2];
		visit = new boolean[n + 2][n + 2];

		int count = 0; // 단지의 수
		int[] houseNum = new int[n * n + 2]; // 각 단지의 집의 수를 저장할 배열

		for (int i = 0; i < n; i++) { // arr에 입력받은 집의 모양 삽입
			String tmp = br.readLine();
			for (int j = 0; j < n; j++) {
				arr[i][j] = tmp.charAt(j) - '0';
			}
		}

		for (int i = 0; i < n; i++) { // bfs방식으로 구하기
			for (int j = 0; j < n; j++) {
				if (arr[i][j] == 0 || visit[i][j] == true)
					continue;
				count++;
				Queue<Location> Q = new LinkedList<>();
				visit[i][j] = true;
				Q.offer(new Location(i, j));
				int house = 1;
				while (!Q.isEmpty()) {
					Location location = Q.poll();
					int row = location.row;
					int col = location.col;

					for (int k = 0; k < 4; k++) {
						int tmpX = row + dx[k];
						int tmpY = col + dy[k];

						if (tmpX < 0 || tmpX >= n || tmpY < 0 || tmpY >= n)
							continue;
						if (visit[tmpX][tmpY] == true || arr[tmpX][tmpY] == 0)
							continue;
						visit[tmpX][tmpY] = true;
						Q.offer(new Location(tmpX, tmpY));
						house++;
					}
				}
				houseNum[count - 1] = house; // houseNum에 각 단지의 집의 개수 저장
			}
		}

		//왜 counting의 배열의 크기가 n*n이면 안될까? -> array 런타임에러 발생
		int[] counting = new int[n * n + 1];
		for (int i = 0; i < n * n; i++) {
			if (houseNum[i] != 0)
				counting[houseNum[i]]++;
			;
		} // 카운팅정렬에 값 입력
		sb.append(count).append("\n");
		//왜 i의 범위가 n*n+1 미만일때가 맞을까? --> n*n으로 할때는 답이 틀림.
		for (int i = 0; i < n * n + 1; i++) {
			while (counting[i] > 0) {
				sb.append(i).append("\n");
				counting[i]--;
			}
		}
		System.out.print(sb);

		/*
		 sb.append(count).append("\n"); 
		 Arrays.sort(houseNum); for(int i=0;
		 i<houseNum.length; i++) { if(houseNum[i] != 0)
		 sb.append(houseNum[i]).append("\n"); } System.out.print(sb);
		 */

	}
}
