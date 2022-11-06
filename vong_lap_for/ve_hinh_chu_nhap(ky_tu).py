char = input("Your char: ")
width = int(input("Width: "))
height = int(input("Height: "))

for i in range(1, height + 1):
    hinh = ""
    for j in range(1, width + 1):
        if i == 1 or i == height:
            hinh = hinh + char
        else:
            if j == 1 or (j == width):
                hinh = hinh + char
            else:
                hinh = hinh + " "
    print(hinh)
                
                
