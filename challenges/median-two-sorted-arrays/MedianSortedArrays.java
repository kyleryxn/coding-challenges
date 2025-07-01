class MedianSortedArays {
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
}