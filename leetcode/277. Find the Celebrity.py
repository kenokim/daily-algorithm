# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        a = 0
        b = 1
        while b < n:
            if knows(a, b):
                a = b
                b = b + 1
            else:
                b += 1
        
        candidate = a
        
        for b in range(n):
            if b != candidate:
                if not knows(b, candidate):
                    return -1
                
                if knows(candidate, b):
                    return -1

        return candidate

# 2 for loops -> O(N^2)
# celebrity = all the others know him, but he does not know any or them.
