"""

we make a for loop until everyone is removed from deque

make a condition where at position k, it gets the name of the customer and the amount of tickets they want 

if they have more or equal to 1, subtract by one and move their name to the back of the deque ( popleft and append )


for _ in q.len + 1:

    if q:
    

    if tickets[i] >= 1:
        tickets -= 1
        q.append(tickets[i])
        k++


    else:
        return k

"""

from collections import deque as d


def time_required_to_buy(tickets, k):

    q = d(range(len(tickets)))

    print(q)


ticket = [2,3,6,7,4]

time_required_to_buy(ticket, 1)


