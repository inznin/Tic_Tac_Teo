# 🎮 Mastermind Game
# 🧠 ABZUMS AI - Phase 3
# 👩‍💻 Naznin Hoseini

import requests

# --- Start a new game  ---
def start_game():
    url = "https://mastermind.darkube.app/game" 
    response = requests.post(url)
    data = response.json()
    return data["game_id"]


# --- Send a guess and return black & white counts ---
def send_guess(game_id, guess):
    url = "https://mastermind.darkube.app/guess"
    data = {
        "game_id": game_id,
        "guess": guess
    }
    response = requests.post(url, json=data)
    result = response.json()
    return result["black"], result["white"]


# --- Get user guess ---
def prompt_guess(game_id):
    while True:
        guess = input("Enter 4 unique digits from 1 to 6: ")

        if len(guess) != 4:
            print("❌ Guess must be exactly 4 digits.")
            continue

        valid_digits = "123456"
        for digit in guess:
            if digit not in valid_digits:
                print("❌ Please use digits from 1 to 6.")
                break
        else:
            if len(set(guess)) != 4:
                print("❌ Digits must be unique.")
                continue

            black, white = send_guess(game_id, guess)
            print(f"⚫ Black: {black}   ⚪ White: {white}")

            if black == 4:
                print("🎉 You guessed the code! ✨")
                break


# --- Run the game ---
def run_game():
    print("🎮 Welcome to Mastermind!")
    print("🎯 Guess the 4-digit code using digits 1 to 6.")
    print("⭕ Digits must be unique.\n")

    game_id = start_game()
    prompt_guess(game_id)


run_game()