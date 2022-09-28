data = dict()

data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

print(data)

if '사과' in data:
    print('apple')

print(data.keys())
print(data.values())

keys = data.keys()
print(keys)

for key in keys:
    print(key)

data = set([1, 1, 2, 2, 3, 4, 5])
print(data)

data = {1, 1, 2, 2, 3, 4, 5}
print(data)

a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 5, 8}

print(a | b)
print(a & b)
print(a - b)

a.add(6)
b.update([13, 21])
a.remove(1)

print(a, b)






























