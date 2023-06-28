"""
Problem Statement
Statement
Given a sentence, reverse the order of its words without affecting the order of letters within a given word.

Constraints:

Sentence contains English uppercase and lowercase letters, digits, and spaces.
- 1 <= sentence.length <= 10^4
- The order of the letters within a word is not to be reversed.
Note: The input string may contain leading or trailing spaces or multiple spaces between words. The returned string, however, should only have a single space separating each word. Do not include any extra spaces.

Test Case:
Input String
"Hurray 3 2 1 world"
Reversed String
"world 1 2 3 Hurray"

"""
def reverse_words(sentence):
    # write you code
    r = len(sentence) - 1
    l = r 
    result = ''
    while l >= 0:
        if l==r and sentence[l] == ' ':
            l = l-1
            r=l
            continue
        
        if sentence[l] == ' ':
            result = result + sentence[l+1:r+1] + ' '
            r = l-1

        if l == 0:
            result = result + sentence[l:r+1]
            r=len
    
        l = l-1
    return result

print(reverse_words("1 2 3 Hurray"))