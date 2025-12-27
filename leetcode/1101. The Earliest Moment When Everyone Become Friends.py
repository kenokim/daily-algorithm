class Solution:
    def is_all_friend(self, uf):
        for i in uf:
            if i != uf[0]:
                return False

        return True

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])
        uf = list(x for x in range(n))
        
        for log in logs:
            ts = log[0]
            a = log[1]
            b = log[2]
            group_b = uf[b]    
            for i in range(n):
                if uf[i] == group_b:
                    uf[i] = uf[a]
            
            if self.is_all_friend(uf):
                return ts
        
        return -1

# logs 가 지나감에 따라 같은 그룹으로 묶어야 한다.
# [0, 0, 2, 3, 4, 5]
# [0, 0, 2, 3, 3, 5]
# n < 100, O(N) * 100