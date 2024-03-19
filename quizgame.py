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
    {"question": "What is the largest planet in our solar system?", "choices": ["Mars", "Jupiter", "Earth", "Saturn"], "answer": "2"},
    {"question": "Who wrote 'Hamlet'?", "choices": ["Charles Dickens", "William Shakespeare", "Leo Tolstoy", "Mark Twain"], "answer": "2"},
    {"question": "What is the chemical symbol for water?", "choices": ["O2", "H2O", "CO2", "NaCl"], "answer": "2"},
    {"question": "What year did the Titanic sink?", "choices": ["1912", "1905", "1898", "1923"], "answer": "1"},
    {"question": "What is the speed of light in vacuum?", "choices": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s"], "answer": "1"},
    {"question": "Who painted the Mona Lisa?", "choices": ["Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "answer": "3"},
    {"question": "What is the capital of Japan?", "choices": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "answer": "3"},
    {"question": "How many continents are there on Earth?", "choices": ["5", "6", "7", "8"], "answer": "3"},
    {"question": "What is the largest ocean on Earth?", "choices": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "4"}
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
