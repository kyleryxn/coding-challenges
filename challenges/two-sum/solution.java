import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] array, int targetSum) {
        Map<Integer, Integer> prevMap = new HashMap<>();
        
        for (int i = 0; i < array.length; i++) {
            int difference = targetSum - array[i];
            
            if (prevMap.containsKey(difference)) {
                return new int[] {prevMap.get(difference), i};
            }
            
            prevMap.put(array[i], i);
        }
        
        throw new IllegalArgumentException("No match found!");
    }
}