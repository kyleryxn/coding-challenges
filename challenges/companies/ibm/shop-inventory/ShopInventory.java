package challenges.ibm;

import java.util.List;
import java.util.stream.IntStream;

public class ShopInventory {

    public static int getMinMoves(List<Integer> quantity) {

        // Calculate the total sum of items in the inventory
        int totalSum = quantity.stream().mapToInt(Integer::intValue).sum();

        int minMoves = Integer.MAX_VALUE;
        int cumulativeSum = 0;

        // Iterate through item types to find the minimum imbalance
        for (int i = 0; i < quantity.size() - 1; i++) {
            cumulativeSum += quantity.get(i);

            int imbalance = Math.abs(cumulativeSum - (totalSum - cumulativeSum));

            // Update the minimum moves if this imbalance is smaller
            minMoves = Math.min(minMoves, imbalance);
        }

        return minMoves;
    }

    public static int getMinMoves_WithStreams(List<Integer> quantity) {

        // Calculate the total sum of items in the inventory
        int totalSum = quantity.stream().mapToInt(Integer::intValue).sum();

        return IntStream.range(0, quantity.size() - 1)
                .mapToObj(j -> quantity.subList(0, j + 1).stream().mapToInt(Integer::intValue).sum())
                .mapToInt(cumulativeSum -> Math.abs(cumulativeSum - (totalSum - cumulativeSum)))
                .min()
                .orElse(0);
    }

}