import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = s.translate(str.maketrans("", "", string.punctuation + " ")).lower()
        print(clean)
        for i in range(len(clean)):
            if (not clean[i] == clean[(-i-1)]):
                return False
        return True
        