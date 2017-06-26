# Enter your code here. Read input from STDIN. Print output to STDOUT

nums = map(int, raw_input().strip().split(' '))

t1 = nums[0]
t2 = nums[1]
n = nums[2]

def fib(t1, t2):
    return t1 + (t2**2)

def solve(t1, t2, n):

    seq = [t1, t2]

    while len(seq) < n + 1:
        seq.append(fib(seq[-2], seq[-1]))
        if len(seq) == n:
            return seq[-1]

print solve(t1, t2, n)
