import random

class flashcard:
    def __init__(self):
        self.animals = {'Con ong': 'bee',
                        'Con thỏ': 'rabbit',
                        'Con cua': 'crab',
                        'Con mèo': 'cat',
                        'Con ngựa': 'horse',
                        'Con khỉ': 'monkey',
                        'Con lừa': 'donkey'}
    def quiz(self):
        while True:
            vietnamese, english = random.choice(list(self.animals.items()))
            print("Tiếng anh của từ {} là: ".format(vietnamese))
            user_answer = input()
        
            if user_answer.lower() == english:
                print("Đúng")
            else:
                print("Sai")
        
            y_o_n = input("Bạn có muốn tiếp tục không?(Y/N)")
            if y_o_n.upper() == "N":
                break
        print("Kết thúc")
        
fc = flashcard()
fc.quiz()
