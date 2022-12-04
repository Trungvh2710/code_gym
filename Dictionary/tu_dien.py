dictionary = {
            "abandon": "từ bỏ",
            "act": "hành động",
            "afraid": "sợ hãi",
            "against" : "chống lại",
            "agree" : "đồng ý",
            "allow" : "cho phép" 
           }
def get_translate(translate_word):
    if translate_word in dictionary:
        print(translate_word, ":", dictionary[translate_word])
    else:
        print("Từ bạn cần tìm kiếm không có trong từ điển")
while True:
    translate_word = input("Nhập từ bạn cần tra cứu: ")
    get_translate(translate_word)
    y_o_n = input("Bạn có muốn tiếp tục tra cứu không?(Y/N)")
    if y_o_n.upper() == "N":
        break