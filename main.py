n = int(input("Введіть розмір масиву: "))
arr = []

print("Введіть елементи масиву:")
for _ in range(n):
    arr.append(int(input()))

zero_indices = [i for i, x in enumerate(arr) if x == 0]

if len(zero_indices) == 0:
    print("Нульові елементи відсутні в масиві.")
else:
    print("Індекси нульових елементів:", *zero_indices)
