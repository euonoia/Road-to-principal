def defang(s):
    length = len(s)
    i = 0
    result = ""  
    
    # Loop through every character from index 0 to the end
    while i < length:
        
        if s[i] == ' ':
            result = result + "-"
        else:
            result = result + s[i]
            
        i += 1
        
    print(result)


defang("Hello World")