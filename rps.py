"""This program plays a game of Rock, Paper,
Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']


class Player:
    """
    The Player class is the parent class
    for all the Players in this game
    """

    def __init__(self):
        """
        An initializer method that initialized
        score, their_move and index_of_current_move
        to a default value
        """
        self.score = 0
        self.their_move = random.choice(moves)
        self.index_of_current_move = 0

    def move(self):
        """
        An empty method to be inherited by subclasses.
        """

    def learn(self, their_move):
        """
        Learn other player's move
        Args:
            their_move: a string
        """
        self.their_move = their_move


class RockPlayer(Player):
    """
    A Player subclass, that always play rock.
    """

    def move(self):
        """
        Returns hardcoded player's move as a string 'rock'
        Returns:
            'rock': a string representing the player's move
        """
        return 'rock'


class RandomPlayer(Player):
    """
    A Player subclass, that chooses its move at random.
    """

    def move(self):
        """
        Returns a random choice of move
        Returns:
            random.choice(moves):
                a string representing a random move
                from moves list
        """
        return random.choice(moves)


class HumanPlayer(Player):
    """
    A Player subclass, whose move method asks
    the human user what move to make.
    """

    def move(self):
        """
        Returns user input move
        Returns:
            move.lower():
                a string representing user input
                move in lower case
        """
        move = ''
        while move.lower() not in moves:
            move = input("Rock, paper, scissors? > ")
        return move.lower()


class ReflectPlayer(Player):
    """
    A Player subclass, that remembers
    what move the opponent played last round,
    and plays that move this round.
    """

    def move(self):
        """
        Returns the opponent player's previous move
        Returns:
            self.their_move:
                a string representing opponent
                player's previous move
        """
        return self.their_move


class CyclePlayer(Player):
    """
    A Player subclass, that remembers
    what move it played last round,
    and cycles through the different moves.
    """

    def move(self):
        """
        Returns a cycle of different move from last round
        Returns:
            next_move:
                a string representing of the next cycle move
        """
        next_move = moves[self.index_of_current_move]
        self.index_of_current_move = \
            (self.index_of_current_move + 1) % len(moves)
        return next_move


def beats(one, two):
    """
    Returns a boolean value of
    whether one move beats another one
    Args:
        one: string
        two: string
    Returns:
        beat: a boolean representing the result of beat
    """
    beat = ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))
    return beat


class Game:
    """
    Game Class for both players, keeping moves,
    scores and determines winners.
    """

    def __init__(self, player_1, player_2):
        """
        Game class initializer
        Args:
            player_1: Player object
            player_2: Player object
        """
        self.player_1 = player_1
        self.player_2 = player_2

    def play_round(self):
        """
        Get and learn player's move.
        Get the scores and winners.
        """
        move1 = self.player_1.move()
        move2 = self.player_2.move()
        print(f"You played {move1}.")
        print(f"Opponent played {move2}.")
        self.player_2.learn(move1)

        if move1 == move2:
            print("** TIE **")
        else:
            if beats(move1, move2):
                self.player_1.score += 1
                print("** PLAYER ONE WINS **")
            else:
                self.player_2.score += 1
                print("** PLAYER TWO WINS **")

        print(f"Score: Player One {self.player_1.score}, "
              f"Player Two {self.player_2.score}\n")

    def play_game(self):
        """
        Play 3 rounds of games and
        print the winners with scores.
        """
        print("\nRock Paper Scissors, Go!\n")

        for game_round in range(3):
            print(f"Round {game_round + 1} --")
            self.play_round()

        if self.player_1.score > self.player_2.score:
            print(f"Player One wins with scores: {self.player_1.score}")
        elif self.player_2.score > self.player_1.score:
            print(f"Player Two wins with scores: {self.player_2.score}")
        else:
            print(f"Tie with scores: {self.player_1.score}")
        print("------------------------------")


def get_user_input_strategy():
    """
    Get user input strategy options to play the game
    Returns:
        a string representing of user input strategy
    """
    return input("""
Select the player strategy you want to play against:
1- Rock Player
2- Random Player
3- Cycle Player
4- Reflect Player
> """)


def main():
    """
    Create game object and calls play_game() method.
    """
    strategies = {"1": RockPlayer(),
                  "2": RandomPlayer(),
                  "3": CyclePlayer(),
                  "4": ReflectPlayer()
                  }

    user_choice = ''
    while user_choice.lower() != 'quit':

        user_input = get_user_input_strategy()
        while user_input not in strategies:
            user_input = get_user_input_strategy()

        game = Game(HumanPlayer(), strategies[user_input])
        game.play_game()

        user_choice = input("Enter 'continue' or 'quit' > ")
        while user_choice.lower() != 'continue' and \
                user_choice.lower() != 'quit':
            user_choice = input("Enter 'continue' or 'quit' > ")
        print("------------------------------")


if __name__ == '__main__':
    main()
