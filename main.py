import art
import game_data
import random

game_data_list = game_data.data[:]

def compare_option():
    random.shuffle(game_data_list)
    game_data_item = game_data_list.pop()
    return game_data_item['name'], \
           game_data_item['follower_count'], \
           game_data_item['country'], \
           game_data_item['description']

def high_low():
    counter = 0
    while True:
        if counter == 3:
            print("You win!")
            break

        if len(game_data_list) < 2:
            print("Not enough data to continue the game.")
            break

        option_a = compare_option()
        option_b = compare_option()

        print(f"Compare A: {option_a[0]}, {option_a[3]}, from {option_a[2]}.\n")
        print(art.vs)
        print(f"Compare B: {option_b[0]}, {option_b[3]}, from {option_b[2]}.\n")

        while True:
            user_input = input("Who has more followers? Type 'A' or 'B'.\n").lower()
            if user_input not in ['a', 'b']:
                print("Please choose a valid option.")
            else:
                break

        if user_input == 'a':
            if option_a[1] > option_b[1]:
                counter += 1
                print(f"Correct! {option_a[0]} has a larger following than {option_b[0]}. \nCurrent Score is {counter}\n")
            else:
                print(f"Wrong! {option_a[0]} has a smaller following than {option_b[0]}. \nCurrent Score is {counter}\n")
                break
        elif user_input == 'b':
            if option_b[1] > option_a[1]:
                counter += 1
                print(f"Correct! {option_b[0]} has a larger following than {option_a[0]}. \nCurrent Score is {counter}\n")
            else:
                print(f"Wrong! {option_b[0]} has a smaller following than {option_a[0]}. \nCurrent Score is {counter}\n")
                break

high_low()
