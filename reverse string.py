class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while(i < j):
            spare = s[i]
            s[i] = s[j]
            s[j] = spare
            i+=1
            j-=1
