class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        top_k = [key for key, count in sorted(freq.items(), key=lambda item: item[1], reverse = True)]
        return top_k[:k]
        