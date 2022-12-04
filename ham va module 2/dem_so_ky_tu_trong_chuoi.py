def count_chuoi(txt):
    result = 0
    for i in txt:
        result += 1
    return result
input_str = input("Your string: ")
print("Do dai chuoi:", count_chuoi(input_str))