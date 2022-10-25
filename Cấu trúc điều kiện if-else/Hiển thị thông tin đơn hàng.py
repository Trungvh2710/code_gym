num = int(input("Số tiền người dùng đã chi: "))
if num >= 150:
    print("Số tiền thành toán :", num-50)
elif num >= 100:
    print("Số tiền thanh toán: ", num-25)
elif num >= 75:
    print("Số tiền thanh toán: ", num-15)
else: 
    print("Số tiền thanh toán: ", num)