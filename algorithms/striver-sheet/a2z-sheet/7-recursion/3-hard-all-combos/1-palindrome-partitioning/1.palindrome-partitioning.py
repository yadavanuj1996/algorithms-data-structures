class Solution:
    result = []

    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        if len(s) == 1:
            return [[s]]
    
        return self.valid_palindrome_partition(s[0:1]+"|"+s[1:])
     

    def is_valid_palindrome(self, arr: list) -> bool:
        for item in arr:
            # checking if a str is palindrome or not
            if not item == item[::-1]:
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