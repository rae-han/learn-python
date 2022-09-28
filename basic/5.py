def add(a, b):
    return a + b

print(add(4, 6))

def add(a, b):
    return a + a + b

print(add(b = 2, a = 1))

count = 0

def func():
    global count
    count += 1

for i in range(10):
    func()

print(count)

print((lambda a, b: a + b)(1, 2))

data = list(map(int, input().split()))
print(data)

import sys
data = sys.stdin.readline().rstrip()
print(data)
for i in data:
    print(i)




