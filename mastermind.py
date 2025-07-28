# game(XO)
# ABZUMS AI Course - Part 3 
# Naznin Hoseini

game_id: "dbnilwkv1rqp"
import requests
def start_game():
    url = "https://mastermind.darkube.app/game" 
    response = requests.post(url)
        
    data = response.json()
    return data["game_id"]
    
def send_guess(game_id , guess):
    url = "https://mastermind.darkube.app/guess"
    data = {"game_id": game_id ,
            "guess" : guess
            }
    response = requests.post(url , json=data)
    result = response.json()
    return result ["black"] , result["white"]

#prompt guess(game_id):
def prompt_guess(game_id):
    while True:
        guess = input("enter 4 unique digits from 1 to 6")

        if len(guess) != 4 :
            print("❌guess must be exactly 4 digits.")
            continue
        
        valid_digits ="123456"
        for digit in guess :
            if digit not in valid_digits:
                print("❌plaese enter digits from 1 to 6")
                break

        if len(set(guess)) != 4 :
            print("❌digits must be unique.")
            continue
        black , white = send_guess(game_id ,guess)

        print(f"black(correct place):{black} , white(correct place):{white}")  

        if black == 4 :
            print("congratulations! you gussed the code✨ ")
            break


# run game
def run_game():
    print("🎮 Welcome to Mastermind!")
    print("🎯 Try to guess the 4-digit code using digits 1 to 6.")
    print("⭕ Digits must be unique (no repeats). Good luck!")
    print("")
    
    game_id = start_game()
    prompt_guess(game_id)

run_game()