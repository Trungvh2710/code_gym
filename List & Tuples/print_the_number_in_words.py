numbers = input("Nhập dãy chữ số: ")
text = ("không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín")
for num in numbers:
    print(text[int(num)], end = " ")