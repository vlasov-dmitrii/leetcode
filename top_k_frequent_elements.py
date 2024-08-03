nums = [1,1,1,2,2,3]
k = 2

def topKFrequent(nums, k):
        integers = {}
        for num in nums:
            if num not in integers:
                integers[num] = 1
            else:
                integers[num] += 1
        
        freq = []
        while k > 0:
            max = 0
            max_key = 0
            for key in integers:
                if integers.get(key) > max:
                    max = integers.get(key)
                    max_key = key
            #print(max_key)
            integers.pop(max_key)
            freq.append(max_key)
            k -= 1
        return freq

print(topKFrequent(nums, k))