score = 100

if score > 95:
    print('A')
elif score >= 90:
    print('B')
elif score > 80:
    print('C')
else:
    pass

print(not True)

if True:
    pass

result = 'Success' if score >= 80 else 'Fail'
print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []

for i in a:
    if i not in remove_set:
        result.append(i)
print(result)

result = [i for i in a if i not in remove_set]
print(result)













