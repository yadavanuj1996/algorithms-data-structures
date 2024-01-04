class Solution:
    result = []

    def partition(self, s: str) -> list[list[str]]:
        self.result = []
        if len(s) == 1:
            return [[s]]
    
        return self.valid_palindrome_partition(s[0:1]+"|"+s[1:])
     

    def is_valid_palindrome(self, arr: list) -> bool:
        def is_palindrome(s: str, l: int, r:int)->bool:
            if not s[l] == s[r]:
                return False
            
            if l<r:
                return is_palindrome(s, l+1, r-1)
            
            return True

        for item in arr:
            if not is_palindrome(item, 0, len(item)-1):
                return False
        
        return True

    def valid_palindrome_partition(self, cur_seq: str):
        if cur_seq[-1] == "|":
                temp_arr = cur_seq[:len(cur_seq)-1].split("|")
                if self.is_valid_palindrome(temp_arr):
                    self.result.append(temp_arr)
                return
        
        index = cur_seq.rfind("|")
        # pick     
        self.valid_palindrome_partition(cur_seq[0:index+2]+"|"+cur_seq[index+2:])   
        self.valid_palindrome_partition(cur_seq[0:index]+cur_seq[index+1:index+2]+"|"+cur_seq[index+2:])
        return self.result

s = "aab"
sol = Solution()
print(sol.partition(s))