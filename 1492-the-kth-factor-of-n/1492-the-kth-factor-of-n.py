class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = defaultdict(int) #index:factor
        idx= 0
        for i in range(1,n+1):
            if n%i==0:
                factors[idx+1]=i
                idx+=1
        return factors.get(k,-1)
            
