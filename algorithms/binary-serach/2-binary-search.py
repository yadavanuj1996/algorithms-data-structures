class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int) -> list[str]:
        self.generatePattern(n, 1, 0, "(")
        return self.result

    def generatePattern(self, n:int, no_of_left_brackets:int, no_of_right_brackets:int, pattern: str):
        if no_of_left_brackets < no_of_right_brackets or no_of_left_brackets > n or no_of_right_brackets > n:
            return
        elif no_of_left_brackets == n and no_of_right_brackets == n: 
            self.result.append(pattern)
            return
        
        self.generatePattern(n, no_of_left_brackets+1, no_of_right_brackets, pattern+'(')
        self.generatePattern(n, no_of_left_brackets, no_of_right_brackets+1, pattern+')')
    

def main():
    n = 3
    sol = Solution()
    print(sol.generateParenthesis(n))


if __name__ == "__main__":
    main()
