class Solution {
public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        long long MOD = 1e9 + 7;
        int n = s.length();
        
        vector<long long> pow10(n + 1, 1);
        for (int i = 1; i <= n; ++i) {
            pow10[i] = (pow10[i - 1] * 10) % MOD;
        }
        
        vector<long long> pref_val(n + 1, 0);
        vector<long long> pref_sum(n + 1, 0);
        vector<int> pref_cnt(n + 1, 0);
        
        for (int i = 0; i < n; ++i) {
            int digit = s[i] - '0';
            if (digit > 0) {
                pref_val[i + 1] = (pref_val[i] * 10 + digit) % MOD;
                pref_sum[i + 1] = pref_sum[i] + digit;
                pref_cnt[i + 1] = pref_cnt[i] + 1;
            } else {
                pref_val[i + 1] = pref_val[i];
                pref_sum[i + 1] = pref_sum[i];
                pref_cnt[i + 1] = pref_cnt[i];
            }
        }
        
        vector<int> ans;
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            int k = pref_cnt[r + 1] - pref_cnt[l];
            
            long long x = (pref_val[r + 1] - (pref_val[l] * pow10[k]) % MOD + MOD) % MOD;
            long long digit_sum = pref_sum[r + 1] - pref_sum[l];
            
            ans.push_back((x * digit_sum) % MOD);
        }
        
        return ans;
    }
};
