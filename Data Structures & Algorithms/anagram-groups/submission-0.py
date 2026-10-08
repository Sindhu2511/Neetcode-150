class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for s in strs:
            new_s = str(sorted(s))
            if new_s not in anagram:
                anagram[new_s] = []
            anagram[new_s].append(s)
        result = [res for res in anagram.values()]
        return result

        