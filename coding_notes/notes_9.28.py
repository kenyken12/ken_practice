print("this is where all coding notes will be uploaded and stores from now on!")


"""

9/28

O(1) = constant time
O(n) = work increases porpotionally
o(n^2) = work increases exponentially 



functions - gets input then returns a output 

function structure 

def (function keyword) printHi (function name) (3) (argument)




recursive functions = functions that call on themselves until the the base condition is met 
"""


def recursive(number):
    if number == 0: #This is our base condition. Since we are assuming that "number" starts as a positive number and that it keeps getting reduced by 1 during the recursion, we know that it will eventually reach zero and therefore, we know that the recursion will stop and not loop infinitely. 
        return
    #print(f"Counting number {number}")
    recursive(number - 1)
    print(f"Counting number {number}")

recursive(10)

