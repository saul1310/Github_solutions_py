def maxOperations(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        co = 0
        for x in nums:
            comp = k - x
            if counter[comp]>0:
                counter[comp]-=1
                co+=1
            else:
                counter[x] +=1
        return co
       