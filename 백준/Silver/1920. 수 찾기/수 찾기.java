import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받음
        int n = Integer.parseInt(br.readLine());

        // N개의 정수 배열을 입력 받음
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // N개의 정수 배열을 오름차순으로 정렬
        Arrays.sort(arr);

        // M 입력 받음
        int m = Integer.parseInt(br.readLine());

        // 결과를 저장하는 StringBuilder
        StringBuilder sb = new StringBuilder();

        // M개의 수들을 입력 받고, 이 수들이 N개의 정수 배열에 존재하는지 확인하여 결과를 StringBuilder에 추가
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int num = Integer.parseInt(st.nextToken());

            // 이진 탐색으로 M개의 수가 N개의 정수 배열에 존재하는지 확인
            sb.append(myBinarySearch(arr, num) + "\n"); // 존재하지 않으면 0을 StringBuilder에 추가
        }

        // 최종 결과 출력
        System.out.println(sb);
    }

    public static int myBinarySearch(int[] arr, int target) {
        int s = 0;
        int e = arr.length - 1;

        while (s <= e) {
            int m = (s + e) / 2;
            if (target == arr[m]) {
                return 1;
            } else if (target < arr[m]) {
                e = m - 1;
            } else {
                s = m + 1;
            }
        }

        return 0;
    }
}
