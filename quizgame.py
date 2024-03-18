class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

def ask_question(question):
    print(question["question"])
    for i, choice in enumerate(question["choices"], 1):
        print(f"{i}. {choice}")
    answer = input("Your answer (1-4): ")
    return answer.strip() == question["answer"]

def main():
    players = []
    num_players = int(input("Enter number of players: "))
    for _ in range(num_players):
        player_name = input("Enter player's name: ")
        players.append(Player(player_name))

    questions = [
        {"question": "What is the capital of France?", "choices": ["Berlin", "London", "Paris", "Rome"], "answer": "3"},
        # Add more questions here
    ]

    for question in questions:
        for player in players:
            print(f"{player.name}'s turn:")
            if ask_question(question):
                print("Correct!")
                player.add_score(1)
            else:
                print("Wrong answer.")
            print()

    winner = max(players, key=lambda p: p.score)
    print(f"The winner is {winner.name} with {winner.score} points!")

if __name__ == "__main__":
    main()
