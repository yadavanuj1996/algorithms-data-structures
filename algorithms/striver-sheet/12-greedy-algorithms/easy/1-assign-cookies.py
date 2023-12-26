class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        cookie_size_len = len(s)
        i,j = 0, 0
        result = 0
        
        while i < len(g):
            greed = g[i]
            if j >= cookie_size_len:
                break
            
            if s[j] >= greed:
                j += 1
                result += 1
            else:
                j += 1
                continue

            i += 1  
            
        return result
    

g = [1,2]
s = [1,2,3]
sol_obj = Solution()
print(sol_obj.findContentChildren(g, s))