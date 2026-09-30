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


