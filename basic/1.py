# # 숫자
# a = 1000
# print(a)
#
# a = -7
# print(a)
#
# a = 0
# print(a)

# # 리스트
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
# print(a[4])
#
# # 빈리스트 선언 방법
# a = list()
# print(a)
#
# # 빈리스트 선언 방법
# a = []
# print(a)

print(a[2:6])

array = [i for i in range(20) if i % 2 == 1]
print(array)

array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

array = [i*i for i in range(1, 10)]
print(array)

print([0]*3)

array = [[0]*4]*3
print(array)

array[1][1] = 2
print(array)

array = [i for i in range(2, 6)]
print(array)

array.append(1)
print(array)
array.sort()
print(array)
array.sort(reverse=True)
print(array)

array.insert(2, 6)
print(array)

print(array.count(2))

array.remove(3)
print(array)

remove_set = [2, 4]

result = [i for i in array if i not in remove_set]
print(result)

data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

tp = (1, 2, 3, 4)
print(tp)









