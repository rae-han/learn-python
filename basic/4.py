i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)

for i in range(1, 10):
    print(i)

scores = [88, 90, 92, 96, 100]

for i in range(len(scores)):
    if scores[i]>80:
        print(i+1, '번 학생은 합격입니다.')





