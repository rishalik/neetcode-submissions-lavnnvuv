from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        for key, val in counter.items():
            buckets[val].append(key)
        
        res = []
        for i in range(n, 0,-1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res

        