def remove_adjacent_duplicates(s):
    for i in range(len(s)-1):
        
        if s[i] == s[i+1]:
            s = s.replace(s[i], "", 2)
            return remove_adjacent_duplicates(s)
    
    return s