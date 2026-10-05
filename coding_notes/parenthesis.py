"""
make a function that checks to see if a valid closed parenthesis is made
1.) make a dictionary with valid pairs
2.) get the string, then check the first index
2.) check the entire string, see if the closing pair is in the string

"""


def isValid(string):
    counter = 0
    stack = []


    valid_pairs = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for i in string:

        #check to see if its a open bracket
        if i in valid_pairs:
            stack.append(i)
            if stack[-1] == valid_pairs[i]:
                stack.pop()
        #check to see if its a closing bracket
        else:
            if stack:
                return False
            else:
                return True





            

keny = "()"

print(isValid(keny))