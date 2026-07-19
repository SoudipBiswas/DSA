class Solution {
public:
    int mySqrt(int x) {

        if (x == 0) {
            return 0;
        }

        int left = 1;
        int right = x;
        int firstTrueIndex = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (mid > x / mid) {
                firstTrueIndex = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        if (firstTrueIndex == -1) {
            return x;
        }
        return firstTrueIndex - 1;
    }
};