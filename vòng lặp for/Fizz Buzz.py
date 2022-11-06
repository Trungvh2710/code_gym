a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
while a > b:
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
else:
    print("Nhập đúng")

for i in range(a, b):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    else:
        print(i)