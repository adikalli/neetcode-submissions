class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().replace(' ','')
        s= re.sub('[^a-zA-Z0-9]','',s)
        return s[::-1]==s
        