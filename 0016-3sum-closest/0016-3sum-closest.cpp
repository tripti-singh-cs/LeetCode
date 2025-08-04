class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int closest = nums[0] + nums[1] + nums[2];  // Initial closest sum

        for(int i = 0; i < n - 2; i++) {
            int left = i + 1, right = n - 1;

            while(left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if(abs(target - sum) < abs(target - closest)) {
                    closest = sum;
                }

                if(sum < target) {
                    left++;
                } else if(sum > target) {
                    right--;
                } else {
                    // Exact match found
                    return sum;
                }
            }
        }

        return closest;
    }
};
