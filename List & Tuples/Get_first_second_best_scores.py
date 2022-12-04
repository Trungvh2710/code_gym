input_string = input('Enter elements of a list separated by space ')
arr = input_string.split()
print("list:", arr)
for i in range(0, len(arr)):
    arr[i] = int(arr[i])
arr.sort()
print("list sắp xếp là:",arr)
print("Hai số lớn nhất là: ", arr[-1], arr[-2])