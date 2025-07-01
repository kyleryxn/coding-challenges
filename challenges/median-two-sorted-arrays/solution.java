class Solution {

    // O((m+n) log(m+n)) time complexity
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] merged = new int[m + n];

        System.arraycopy(nums1, 0, merged, 0, m);
        System.arraycopy(nums2, 0, merged, m, n);
        Arrays.sort(merged);

        int midpoint = merged.length / 2;

        // Even sized array
        if (merged.length % 2 == 0) {
            return (double) (merged[midpoint] + merged[midpoint - 1]) / 2;
        } else {
            return (double) merged[midpoint];
        }
    }


    // Optimal Solution
    // O(log (m+n)) time complexity
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is the smaller array to minimize the binary search space
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.length;
        int n = nums2.length;

        // The total number of elements we want on the left side of the partition
        int totalLeft = (m + n + 1) / 2;

        // Binary search on the smaller array
        int left = 0;
        int right = m;

        while (left <= right) {
            // Partition index for nums1
            int i = left + (right - left) / 2;
            // Partition index for nums2 (complement to reach totalLeft)
            int j = totalLeft - i;

            // Edge values: handle when partition is at the boundary
            int nums1LeftMax = (i == 0) ? Integer.MIN_VALUE : nums1[i - 1];
            int nums1RightMin = (i == m) ? Integer.MAX_VALUE : nums1[i];

            int nums2LeftMax = (j == 0) ? Integer.MIN_VALUE : nums2[j - 1];
            int nums2RightMin = (j == n) ? Integer.MAX_VALUE : nums2[j];

            // Check if we have a valid partition
            if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
                // If the total length is even, return the average of the two middle values
                if ((m + n) % 2 == 0) {
                    int leftMax = Math.max(nums1LeftMax, nums2LeftMax);
                    int rightMin = Math.min(nums1RightMin, nums2RightMin);
                    return (leftMax + rightMin) / 2.0;
                } else {
                    // If odd, return the max of left half
                    return Math.max(nums1LeftMax, nums2LeftMax);
                }
            } else if (nums1LeftMax > nums2RightMin) {
                // Move partition i to the left
                right = i - 1;
            } else {
                // Move partition i to the right
                left = i + 1;
            }
        }

        // Should never reach here if input arrays are sorted
        throw new IllegalArgumentException("Input arrays are not sorted or valid");
    }

}