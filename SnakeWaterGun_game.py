import random
options = {"s": "Snake", "w": "Water", "g": "Gun"}


def games():
    no_of_games = 1
    points1 = 0
    points2 = 0
    print("\t \t \t \t \t \t \t \t \t \tSnake Water Gun\n ")
    while no_of_games <= 10:

        print("Select your player: ")
        for key, value in options.items():
            print("Press", key, "for", value, "\n", end="")

        options_name = str(input()).lower()

        while options_name not in list(options.keys()):
            print("wrong input!")
            print("Try Again!: ")
            options_name = str(input()).lower()

        print("User Player : ", options[options_name], "\n", end="")
        lis = list(options.values())
        choice = random.choice(lis)
        print("Computer Player : ", choice, "\n", end="")

        if choice == options[options_name]:
            print("Try again! \n \n")
        else:
            if choice == "Snake" and options[options_name] == "Water":
                points1 += 1
                print(choice, "Computer Wins!", points1, "points earned.", "\n", end="")
                print("\n")

            elif choice == "Water" and options[options_name] == "Gun":
                points1 += 1
                print(choice, "Computer Wins!", points1, "points earned.", "\n", end="")
                print("\n")

            elif choice == "Gun" and options[options_name] == "Snake":
                points1 += 1
                print(choice, "Computer Wins!", points1, "points earned.", "\n", end="")
                print("\n")

            else:
                points2 += 1
                print(options[options_name], "Player Wins!", points2, "points earned.", "\n", end="")
                print()

        print(no_of_games, " Numbers of Games Played.")
        no_of_games += 1

    if no_of_games > 10:
        print("Game Over!")
        print(points1, "Points earned by Computer.")
        print(points2, "Points earned by Player.")
        if points1 == points2:
            print("Tie.")
        elif points1 > points2:
            print("Computer Won the Game.")
        else:
            print("Player won the Game.")


games()
