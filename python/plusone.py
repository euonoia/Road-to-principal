def plusOne(digits):

    for i in range(len(digits)-1,-1,-1):
        if digits[i] < 9:
            digits[i] += 1
            return print(digits)
        else:
            digits = 0
        
        return[1] + digits
plusOne([9])