#!/usr/bin/env python
from wargame import WarGame


def play_war_game():
    """Command Line Interface for the War Game"""
    game = WarGame()
    print("Instructions:")
    print("Press P to play one round, F to complete the full game, E to exit\n")
    possible_inputs = ["P", "E", "F"]

    while True:
        user_input = input("\nEnter P, E or F:")
        if user_input not in possible_inputs:
            print("Invalid input. Try again.")
            continue
        elif user_input == "P":
            game.play()
        elif user_input == "F":
            while True:
                game.play()
        elif user_input == "E":
            print("Thank you for trying out this game")
            exit()


if __name__ == "__main__":
    play_war_game()

