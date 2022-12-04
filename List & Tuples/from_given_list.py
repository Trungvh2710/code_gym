gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]
text = []
number = []
for ele in gadgets:
    if isinstance(ele, str):
        text.append(ele)
    else:
        number.append(ele)
print("List chứa chuỗi:", text)
print("List chứa số:", number)

#Sắp xếp chuỗi
text.sort()
print("List chuỗi sắp xếp theo thứ tự tăng dần:", text)
text.sort(reverse = True)
print("List chuỗi sắp xếp thoe thứ tự giảm dần:", text)

#Sắp xếp số
number.sort()
print("List số sắp xếp theo thứ tự tăng dần:", number)
number.sort(reverse = True)
print("List số sắp xếp thoe thứ tự giảm dần:", number)