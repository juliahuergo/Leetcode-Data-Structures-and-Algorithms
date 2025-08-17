class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ran = Counter(ransomNote)
        mag = Counter(magazine)
        for letter in ran:
            if mag[letter] < ran[letter]:
                return False
        
        return True
        
