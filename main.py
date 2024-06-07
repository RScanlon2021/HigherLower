import game_data
import art
import random

game_data_list = game_data.data

def compare_option(option):
  random.shuffle(game_data_list)
  game_data_item = game_data_list.pop()
  if option == 'A' or option == 'B':
    return game_data_item['name'], \
           game_data_item['follower_count'], \
           game_data_item['country'], \
           game_data_item['description']
  else:
      raise ValueError("Invalid option. Choose 'A' or 'B'.")

def high_low():
  counter = 0
  while True:
    if counter == 3:
      print("You win!")
      break
      
    option_a = compare_option('A')
    option_b = compare_option('B')
    
    print(f"Compare A: {option_a[0]}, {option_a[3]}, from {option_a[2]}.\n")
    print(art.vs)
    print(f"Compare B: {option_b[0]}, {option_b[3]}, from {option_b[2]}.\n")
  
    user_input = input("Who has more followers? Type 'A' or 'B'.\n").lower()
    if user_input not in ['a','b']:
      print("Please choose a valid option.")
    elif user_input == 'a':
      if option_a[1] > option_b[1]:
        counter += 1
        print(f"Correct! {option_a[0]} has a larger following than {option_b[0]}. \nCurrent Score is {counter}\n")
      else:
        print(f"Wrong! {option_a[0]} has a smaller following than {option_b[0]}. \nCurrent Score is {counter}\n")
    elif user_input == 'b':
      if option_b[1] > option_a[1]:
        counter += 1
        print(f"Correct! {option_b[0]} has a larger following than {option_a[0]}. \nCurrent Score is {counter}\n")
      else:
        print(f"Wrong! {option_b[0]} has a smaller following than {option_a[0]}. \nCurrent Score is {counter}\n")
      
high_low()