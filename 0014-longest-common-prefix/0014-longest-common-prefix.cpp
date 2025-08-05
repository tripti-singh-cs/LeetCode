

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";

        string prefix = strs[0]; // Take the first string as base

        for (int i = 1; i < strs.size(); ++i) {
            // Reduce prefix until it matches the beginning of strs[i]
            while (strs[i].find(prefix) != 0) {
                prefix = prefix.substr(0, prefix.length() - 1);
                if (prefix.empty()) return "";
            }
        }

        return prefix;
    }
};


