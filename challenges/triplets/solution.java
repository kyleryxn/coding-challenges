package ibm;

import java.util.Collections;
import java.util.List;

public class Triplets {

    // O(n^3) time complexity
    public long getTriplets(int constraint, List<Integer> numbers) {
        int length = numbers.size();
        long count = 0;

        Collections.sort(numbers);

        for (int i = 0; i < length; i++) {
            for (int j = i + 1; j < length; j++) {
                for (int k = j + 1; k < length; k++) {
                    if (numbers.get(i) + numbers.get(j) + numbers.get(k) <= constraint) {
                        //System.out.println(numbers.get(i) + " " + numbers.get(j) + " " + numbers.get(k));
                        count++;
                    }
                }
            }
        }

        return count;
    }

    // O(n^2) time complexity
    public long getTriplets(int constraint, List<Integer> numbers) {
        int n = numbers.size();
        long count = 0;

        Collections.sort(numbers); // O(n log n)

        for (int i = 0; i < n - 2; i++) {
            int j = i + 1;
            int k = n - 1;

            while (j < k) {
                int sum = numbers.get(i) + numbers.get(j) + numbers.get(k);
                if (sum <= constraint) {
                    // All combinations from j to k-1 with i and j are valid
                    count += (k - j);
                    j++;
                } else {
                    k--;
                }
            }
        }

        return count;
    }

}
