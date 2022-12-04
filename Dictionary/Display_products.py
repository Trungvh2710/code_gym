products = {
            'SMART WATCH': 550,
            'PHONE' : 1000,
            'PLAYSTATION': 500,
            'LAPTOP' : 1550,
            'MUSIC PLAYER' : 600,
            'TABLET' : 400 
           }
def display_product(products, price):
    for key in products:
        if products[key] <= price:
            print(key, ":", products[key])
input_price = int(input("Nhập số tiền: "))
display_product(products,input_price)