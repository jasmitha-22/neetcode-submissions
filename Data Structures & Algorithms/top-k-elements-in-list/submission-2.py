from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #frequency map
        countOfNums = defaultdict(int)

        for num in nums:
            countOfNums[num]+=1

        #bucket sort
        #we want to buckets for how many ever elements there are iin nums
        frequency_buckets = [[] for _ in range(len(nums)+1)]

        for key, value in countOfNums.items():
            frequency_buckets[value].append(key)
        
        solutions = []
        
        for i in range(len(frequency_buckets)-1, 0, -1):
            for n in frequency_buckets[i]:
                solutions.append(n)
                if len(solutions)==k:
                    return solutions;

