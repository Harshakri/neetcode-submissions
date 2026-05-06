class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int og_length = nums.size();
        vector<int> ans(2 * og_length);
        for(int i = 0; i < og_length; ++i) {
            ans[i] = ans[i + og_length] = nums[i];
        }
        return ans;
    }
        
};