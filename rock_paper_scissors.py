import random

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

user_score = 0
computer_score = 0

print("🎮 Welcome to Rock-Paper-Scissors Game!")
print("Instructions: Type rock, paper, or scissors")

while True:
    user_choice = input("\nEnter your choice: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"👤 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)

    if result == "tie":
        print("🤝 It's a tie!")
    elif result == "user":
        print("🎉 You win this round!")
        user_score += 1
    else:
        print("😢 Computer wins this round!")
        computer_score += 1

    print(f"📊 Score → You: {user_score} | Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! 👋")
        break
