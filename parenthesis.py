"""
make a function that checks to see if a valid closed parenthesis is made
1.) make a dictionary with valid pairs
2.) get the string, then check the first index
2.) check the entire string, see if the closing pair is in the string

"""


def isValid(string):
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack = []
    for i in string:
        #check if its a opener and adds it to the stack
        if i in pairs:

            if stack == i:
                stack.pop()
            else: 
                return False
        else:
            stack.append(i)

        if not stack:
            return True
        else:
            return False



    
            



        
    



keny = "()" # true
keny2 = "((())" #false

print(isValid(keny))
print(isValid(keny2))