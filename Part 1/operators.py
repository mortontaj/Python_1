import math


a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down towards mimus infinity
print(a % b)    # 0 modulo: the remainder after integer division

print()

for i in range(1, a//b):
    print(i)

Unit_Price = 2.4
Their_disposable_income = 15
x = Unit_Price
y = Their_disposable_income
print(math.floor(y / x))
print()
print(int(y // x))

print(a + b / 3 - 4 * 12)
print(a + (b/3) - (4 * 12))
print((((a + b)/3)-4)*12)
print(((a + b)/3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()
print(a / (b * a) / b)
