#10
#1 97
#2
#1 20
#2
#1 26
#1 20
#2
#3
#1 91
#3


moves = int(raw_input())
stack = []
ops = []
for _ in range(moves):
    move = map(int, raw_input().split(' '))
    ops.append(move)


for x in ops:
    if len(x) == 2:
        stack.append(x[1])
    else:
        if x[0] == 2:
            stack.pop()
        elif x[0] == 3:
            print max(stack)
