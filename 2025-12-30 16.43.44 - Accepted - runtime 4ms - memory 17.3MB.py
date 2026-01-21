class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        from collections import Counter
        freq = Counter(nums)
        result = 0
        for num, count in freq.items():
            if count % k == 0:
                result += num * count
        return result