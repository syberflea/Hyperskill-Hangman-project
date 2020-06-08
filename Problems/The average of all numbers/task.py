a = int(input())
b = int(input())
segment = list(range(a, b+1))
summa = 0
count = 0
for n in segment:
    if n % 3 == 0:
        summa += n
        count += 1

print(summa / count)