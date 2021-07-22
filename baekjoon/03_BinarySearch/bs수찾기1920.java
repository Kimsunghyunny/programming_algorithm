package tt;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		int[] a = new int[n];
		
		for (int j = 0; j < n; j++) {
			a[j] = Integer.parseInt(st1.nextToken());
		}
		Arrays.sort(a);
		
		int m = Integer.parseInt(br.readLine());
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		
		// binary Search

			for(int j=0; j<m; j++) {
				int x = Integer.parseInt(st2.nextToken());
				int st = -1;
				int en = n;
				
				int result = 0;
				
				while(en-st >1) {
					int mid = (st+en)/2;
					
					if(x == a[mid]) {
						result = 1;
						break;
					}
					if(x < a[mid]) {
						en = mid;
					}
					else if(x > a[mid]) {
						st = mid;
					}
				}
				sb.append(result).append("\n");
			}
		System.out.print(sb);
	}
	
}
