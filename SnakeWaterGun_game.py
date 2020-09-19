import random
options = {"s": "Snake", "w": "Water", "g": "Gun"}


def games():
    no_of_games = 1
    points1 = 2
    points2 = 2
    while no_of_games <= 10:

        print("Select your player: ")
        for key, value in options.items():
            print("Press", key, "for", value, "\n", end="")

        options_name = input()
        # if options_name is not "s" or "w" or "g":
        #     print("Wrong Input!")
        #     options_name = input("Select your player: ")

        print("User Player : ", options[options_name], "\n", end="")
        lis = list(options.values())
        choice = random.choice(lis)
        print("Computer Player : ", choice, "\n", end="")
        if choice == options[options_name]:
            print("Try again!")
        else:
            if choice == "Snake" and options[options_name] == "Water":
                print(choice, "Computer Wins!", points1, "points earned.", "\n", end="")
                print()
                points1 += 1
            elif choice == "Water" and options[options_name] == "Gun":
                print(choice, "Computer Wins!", points1, "points earned.", "\n", end="")
                print()
                points1 += 1
            elif choice == "Gun" and options[options_name] == "Snake":
                print(choice, "Computer Wins!", points1, "points earned.", "\n", end="")
                print()
                points1 += 1

            else:
                print(options[options_name], "Player Wins!", points2, "points earned.", "\n", end="")
                print()
                points2 += 1

                # points1 += 1

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
