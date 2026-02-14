import random

def create_table():
    numbers = random.sample(range(1, 51), 15)
    table = []
    index = 0

    for i in range(3):
        row = []
        for j in range(5):
            row.append(numbers[index])
            index += 1
        table.append(row)

    return table


def create_main_sequence():

    choice = input("Do you want to add main numbers yourself? (yes/no): ").lower()

    if choice == "yes":
        main = []
        print("Enter 5 unique numbers (1-50):")

        while len(main) < 5:
            num = int(input(f"Enter number {len(main)+1}: "))
            if 1 <= num <= 50 and num not in main:
                main.append(num)
            else:
                print(" Invalid number!")

        return main
    else:
        return random.sample(range(1, 51), 5)


def get_players():

    players = {}
    total = int(input("Enter number of players: "))

    for i in range(1, total + 1):

        name = input(f"\nEnter name of Player-{i}: ")

        print(f"{name}, choose 5 unique numbers (1-50): ")

        choices = []

        while len(choices) < 5:
            num = int(input(f"Enter number {len(choices)+1}: "))

            if 1 <= num <= 50 and num not in choices:
                choices.append(num)
            else:
                print(" Invalid number!")

        players[name] = {
            "numbers": choices,
            "score": 0,
            "matched_numbers": []
        }

    return players


def start_game():

    print("\n ~: SEQUENCE MATCH GAME (1-50) :~\n")

    main = create_main_sequence()
    players = get_players()


    view_choice = input("\nDo you want to see other players numbers? (yes/no): ").lower()

    if view_choice == "yes":
        for name, data in players.items():
            print(f"{name} chose: {data['numbers']}")

    print("\nGame Started!\n")

    winner = None

    for player, data in players.items():

        user_sequence = data["numbers"]
        matched = []

        for num in user_sequence:
            if num in main:
                matched.append(num)

        data["score"] = len(matched)
        data["matched_numbers"] = matched

        if len(matched) == 5:
            winner = player

    print("\n ~: RESULT :~")

    if winner:
        print(" Winner is:", winner)
    else:
        print(" No full match winner.")

    print("\nMain Sequence Was:", main)

    print("\nMatch Details:")
    for name, data in players.items():
        print(f"\n{name}")
        print("Matched Count:", data["score"])
        print("Matched Numbers:", data["matched_numbers"])


start_game()
