def is_palindrome(s):
    return True if s == s[::-1] else False

def longest_palindromic_substring(s):
    longest = ""
    
    for start in range(len(s)):
        for end in range((start+1), (len(s)+1)):
            
            substring = s[start:end]
            if len(substring) > len(longest) and is_palindrome(substring):
                longest = substring
    
    return longest if len(longest) >= 2 else ""