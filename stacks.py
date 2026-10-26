stack = []



stack.append("k")
stack.append("e")
stack.append("n")
stack.append("y")

top = stack[-1]


for _ in range(4):
    stack.pop()


empty = not bool(stack)

print(f"is there nothing" + empty)



variable = [{
    "ken": 123,
    "keny": 456,
    "keneth": 789
},{
    "k": 987,
    "e": 654,
    "n": 321
}]


