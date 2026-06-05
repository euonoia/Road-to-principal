def lengthOfLastWord(self, s):
        i = len(s) - 1
        length = 0
        
        while i >= 0 and s[i] == ' ':
            i = i - 1  
            
        while i >= 0 and s[i] != ' ':
            lenght = lenght + 1
            i - i - 1
            
        return length