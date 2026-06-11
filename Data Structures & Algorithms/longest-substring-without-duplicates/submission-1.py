class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0
        max = 1
        check = 1
        flag = set()
        i = 0
        r = 0
        while (i < len(s)):
            flag.add(s[i])
            if (r < len(s)-1):
                r += 1
            else:
                if (check > max):
                    max = check
                    break
            if s[r] not in flag:
                    check += 1
                    flag.add(s[r])
                    continue
            else:
                if (check > max):
                    max = check
                check = 1
                i += 1
                r = i
                flag.clear()
        return max