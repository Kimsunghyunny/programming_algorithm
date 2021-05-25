package Main;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
	class Node {
		String next;
		int edge;

		public Node(String next, int edge) {
			this.next = next;
			this.edge = edge;
		}
	}

	public int solution(String begin, String target, String[] words) {
		int answer = 0;

		if (check2(target, words) != -1) {
			answer = bfs(begin, target, words);
		}
		return answer;
	}
	
	public int bfs(String begin, String target, String[] words) {
		int answer = 0;
		Queue<Node> q = new LinkedList<>();

		boolean[] isAdd = new boolean[words.length];
		q.add(new Node(begin, 0));

		while (!q.isEmpty()) {
			Node n = q.poll();

			if (n.next.equals(target)) {
				answer = n.edge;
				break;
			}

			for (int i = 0; i < words.length; i++) {
				if (!isAdd[i] && check(n.next, words[i])) {
					isAdd[i] = true;
					q.add(new Node(words[i], n.edge + 1));
				}
			}
		}
		return answer;
	}

	public boolean check(String checkWord, String word) {
		int diff = 0;
		for (int i = 0; i < checkWord.length(); i++) {
			if (checkWord.charAt(i) != word.charAt(i))
				diff++;
		}
		if (diff == 1)
			return true;
		else
			return false;
	}

	public int check2(String begin, String[] words) {
		for (int i = 0; i < words.length; i++) {
			if (begin.equals(words[i]))
				return 1;
		}
		return -1;
	}
}