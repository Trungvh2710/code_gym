import random
import time

while True:
    current_number = 1
    if random.randint(0,1) == 0:
        current_player = "human"
    else:
        current_player = "computer"
    
    while current_number <= 21:
        print("The current number is", str(current_number))
        
        if current_player == "human":
            print("Nhập 1, 2, 3. Không vượt quá 21. Người chơi vượt quá 21 sẽ thua.")
            player_choice = ""
            while player_choice not in ["1", "2", "3"]:
                player_choice = input("Nhập số của bạn: ")
                
            player_choice = int(player_choice)
            current_number += player_choice
            
            if current_number >= 21:
                print("The current number is", str(current_number))
                print("Bạn đã thua")
                break
            else:
                current_player = "computer"
                
        else:
            computer_choice = random.randint(1,3)
            current_number += computer_choice
            print("Lượt của máy tính. Máy tính chọn", str(computer_choice))
            time.sleep(1)
            
            if current_number >=21:
                print("The current number is", str(current_number))
                print("Bạn đã thắng")
                break
            else:
                current_player = "human"
                             
    play_again = input("Bạn có muốn chơi lại không?")
    if play_again == "y":
        continue
    else:
        print("Goodbye")
        break