//  This solution beats 100 percent of users on leet code and runs in 0 ms

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string merged;
        int i =0, j =0;
        while (i<word1.length() && j < word2.length()){
            merged += word1[i++];
            merged += word2[j++];

        }
        while ( i < word1.length()){
            merged += word1[i++];
        }

        while (j < word2.length()){
            merged += word2[j++];
        }
        return merged;
        
    }
};