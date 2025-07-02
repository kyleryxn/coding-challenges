import java.util.*;

public class ProfitTargets {

    // O(n log n) time complexity
    public int stockPairs(int target, List<Integer> stocksProfit) {
        int count = 0;
        Map<Integer, Integer> map = new HashMap<>();

        Collections.sort(stocksProfit);

        for (Integer current : stocksProfit) {

            if (map.containsKey(current)) {
                map.put(current, map.get(current) + 1);
            } else {
                map.put(current, 1);
            }
        }

        for (Map.Entry<Integer, Integer> it : map.entrySet()) {
            int i = it.getKey(); // Stores key value of map

            if (2 * i == target) {
                if (map.get(i) > 1) {
                    count += 2;
                }
            } else {
                if (map.containsKey(target - i)) {
                    count++;
                }
            }
        }

        count /= 2;

        //System.out.println(map.entrySet());
        return count;
    }

    // O(n) time complexity
    public int stockPairs(int target, List<Integer> stocksProfit) {
        Set<Integer> seen = new HashSet<>();
        Set<Integer> used = new HashSet<>();
        int count = 0;

        for (int profit : stocksProfit) {
            int complement = target - profit;

            if (seen.contains(complement)
                    && !used.contains(profit)
                    && !used.contains(complement)) {
                count++;
                used.add(profit);
                used.add(complement);
            }

            seen.add(profit);
        }

        return count;
    }
}
