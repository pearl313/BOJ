import java.util.*;
import java.io.*;

public class Main {
//    사용할 변수 선언
    static int n;
    static ArrayDeque<Integer> q;
    static ArrayList<ArrayList<Integer>> graph;
    static int ans = 0;

//    입력받는 함수 만들기
    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
//          미리 선언했던 2차원배열 가져옴
        graph = new ArrayList<>();

        for (int i=0; i < n; i++) {
//            한 줄씩 입력 받으면서,
            String temp = br.readLine();
//            한 줄씩 arrayList 만들고
            ArrayList<Integer> relation = new ArrayList<>();
            for (int j=0; j < n; j++) {
                if (temp.charAt(j) == 'Y') {
                    relation.add(j);
                }
            }
//            2차원 배열에 넣어줌
            graph.add(relation);
        }
        for (int i=0; i < n; i++) {
            bfs(i);
        }
    }

//    bfs 함수
    static void bfs(int v) {
//        deque 선언
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.add(v);
//        visited 배열 선언
        int[] visited = new int[n];
//        visited 배열 초기화
        Arrays.fill(visited, -1);
//        현재 위치 0
        visited[v] = 0;

//        q가 빌 때까지,
        while (!q.isEmpty()) {
//            q의 맨 왼쪽 값 꺼내기
            int cur = q.poll();
//            graph의 해당 인덱스에서 하나씩 돌면서
            for (int i:graph.get(cur)) {
//                방문처리 되어있으면 넘기고
                if (visited[i] != -1) {
                    continue;
                }
//                처리 안된 곳은, 현재 인덱스 값에서 +1 하고 다시 q에 넣어줌
                visited[i] = visited[cur] + 1;
                q.add(i);
            }
        }

//        2-친구 == 거리가 1 또는 2인 것의 개수 확인하기
        int cnt = 0;
        for (int i=1; i < 3; i++) {
            for (int j:visited) {
                if (j == i) {
                    cnt += 1;
                }
            }
        }
        ans = Math.max(ans, cnt);
    }

    public static void main(String[] args) throws IOException {
        input();
        System.out.println(ans);
    }
}
