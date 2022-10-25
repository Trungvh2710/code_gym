a = float(input("Nhập cân nặng: "))
b = float(input("Nhập chiều cao: "))
BMI = a/(b**2)

if BMI >= 40:
    print("Béo phì cấp độ III")
elif BMI >= 35:
    print("Béo phì cấp độ II")
elif BMI >= 30:
    print("Béo phì cấp độ I")
elif BMI >= 25:
    print("Thừa cân")
elif BMI >= 18.5:
    print("Bình thường")
elif BMI >= 17:
    print("Gầy cấp độ I")
elif BMI >= 16:
    print("Gầy cấp độ II")
else:
    print("Gầy cấp độ III")