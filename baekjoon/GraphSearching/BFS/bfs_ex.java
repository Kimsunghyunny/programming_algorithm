package Main;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

import java.io.IOException;

class Location {
	int row, col;

	public Location(int row, int col) {
		this.row = row;
		this.col = col;
	}
}

public class bfs_ex {

	public static int[][] arr;
	static int n, m;
	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static boolean visit[][];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		arr = new int[n + 2][m + 2];
		visit = new boolean[n + 2][m + 2];

		for (int i = 0; i < n; i++) {
			String tmp = br.readLine();
			for (int j = 0; j < m; j++) {
				arr[i][j] = tmp.charAt(j) - '0';
			}
		} // 입력받은 미로 arr에 저장

		bfs(0, 0);
		System.out.print(arr[n - 1][m - 1]);
	}

	public static void bfs(int x, int y) {
		Queue<Location> queue = new LinkedList<>();

		queue.offer(new Location(x, y));
		visit[x][y] = true;

		while (!queue.isEmpty()) {
			Location location = queue.poll();
			int row = location.row;
			int col = location.col;

			for (int i = 0; i < 4; i++) {
				int tmpX = row + dx[i];
				int tmpY = col + dy[i];

				if (checkLocation(tmpX, tmpY)) {
					queue.offer(new Location(tmpX, tmpY));
					visit[tmpX][tmpY] = true;
					arr[tmpX][tmpY] = arr[row][col] + 1;
				}
			}
		}
	}

	public static boolean checkLocation(int row, int col) {
		if (row < 0 || row >= n || col < 0 || col >= m)
			return false;
		if (visit[row][col] != false || arr[row][col] == 0)
			return false;
		return true;
	}

}