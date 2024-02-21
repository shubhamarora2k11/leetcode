from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ctr_a = Counter(ransomNote)
        ctr_b = Counter(magazine)
        flag = 1
        for i in ctr_a.keys():
            if i not in ctr_b.keys() or ctr_b[i]<ctr_a[i]:
                flag = 0
                break
        del(ctr_a)
        del(ctr_b)
        return True if flag==1 else False
        
