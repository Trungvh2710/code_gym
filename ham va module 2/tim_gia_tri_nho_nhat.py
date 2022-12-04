def find_min_value(list_a):
    min_value = int(list_a[0])
    for i in range(len(list_a)):
        list_a[i] = int(list_a[i])
        if list_a[i] < min_value:
            min_value = list_a[i]
    return min_value
input_string = input('Enter elements of a list separated by space ')
arr = input_string.split()
print('list:', arr)
min_value = find_min_value(arr)
print("Min number:", min_value)