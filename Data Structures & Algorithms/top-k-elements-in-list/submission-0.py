class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # make a dictionary (key value pair)
        freq = [[] for i in range(len(nums)+1)] # make array of empty arrays same length as nums

        for n in nums: # pair num and amount num appears
            count[n] = 1 + count.get(n, 0)
        
        for n,c in count.items(): # make array list with all nums of certain amounts linked to their ammounts
            freq[c].append(n)

        
        answ = [] 
        for i in range(len(freq) - 1, 0, -1): # iterate backwards through array
            for n in freq[i]: # for all the numbers at each count add them to answer
                answ.append(n)
                if len(answ) == k: # return if answer = k
                    return answ