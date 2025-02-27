import datetime
import random
import json
import os

rolls: dict = {}


def main():
    log("App starting up...")

    load_rolls()
    show_header()
    show_leaderboard()

    # NOTE: This doesn't work
    # player1: str, player2: str = get_players()
    player1, player2 = get_players()

    log(f"{player1} has logged in.")

    play_game(player1, player2)
    log("Game over.")


def show_header():
    print("---------------------------")
    print(" Rock Paper Scissors")
    print("  File I/O Edition")
    print("---------------------------")


def show_leaderboard():
    leaders: dict[str, int] = load_leaders()

    # NOTE: This should be a dict or tuple, but PyCharm insists that it should be a string
    #   Debug output: sorted_leaders: [('Computer', 1), ('Me', 1)]
    sorted_leaders: list[str] = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)

    print()
    print("---------------------------")
    print("LEADERS:")
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins:,} -- {name}")
    print("---------------------------")
    print()


def get_players() -> tuple[str, str]:
    p1: str = input("Player 1, what is your name? ")
    p2: str = "Computer"

    return p1, p2


def play_game(player_1: str, player_2: str) -> None:
    log(f"New game starting between {player_1} and {player_2}.")

    wins: dict[str, int] = {player_1: 0, player_2: 0}
    roll_names: list[str] = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll1: str = get_roll(player_1, roll_names)
        roll2: str = random.choice(roll_names)

        if not roll1:
            print("Try again!")
            continue

        log(f"Round: {player_1} roll {roll1} and {player_2} rolls {roll2}")
        print(f"{player_1} roll {roll1}")
        print(f"{player_2} rolls {roll2}")

        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            msg: str = "This round was a tie!"
            print(msg)
            log(msg)
        else:
            msg: str = f'{winner} takes the round!'
            print(msg)
            log(msg)
            wins[winner] += 1

        msg = f"Score is {player_1}: {wins[player_1]} and {player_2}: {wins[player_2]}."
        print(msg)
        log(msg)
        print()

    overall_winner: str = find_winner(wins, wins.keys())
    msg = f"{overall_winner} wins the game!"
    print(msg)
    log(msg)
    record_win(overall_winner)


def find_winner(wins: dict[str, int], names: dict[str, int]) -> str | None:
    best_of: int = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name

    return None


def check_for_winning_throw(player_1: str, player_2: str, roll1, roll2) -> str:
    if roll1 == roll2:
        print("The play was tied!")
        return None

    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        return player_1
    elif roll2 in outcome.get('defeated_by'):
        return player_2

    return None


def get_roll(player_name: str, roll_names):
    print("Available rolls:")
    for index, r in enumerate(roll_names, start=1):
        print(f"{index}. {r}")

    text = input(f"{player_name}, what is your roll? ")
    selected_index = int(text) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {text} is out of bounds!")
        return None

    return roll_names[selected_index]


def load_rolls():
    # NOTE: remind myself of the details of `global`
    global rolls

    directory: str = os.path.dirname(__file__)
    filename: str = os.path.join(directory, 'rolls.json')

    with open(filename, 'r', encoding='utf-8') as fin:
        # NOTE: Why won't this work?
        # rolls: dict[str, dict[str, list[str]]] = json.load(fin)
        #
        # rolls: dict[str, dict[str, list[str]]] = json.load(fin)
        #     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # SyntaxError: annotated name 'rolls' can't be global
        rolls = json.load(fin)


    log(f"Loaded rolls: {list(rolls.keys())} from {os.path.basename(filename)}.")


def load_leaders() -> dict[str, int]:
    directory: str = os.path.dirname(__file__)
    filename: str = os.path.join(directory, 'leaderboard.json')

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


def record_win(winner_name):
    leaders: dict[str, int] = load_leaders()

    if winner_name in leaders:
        leaders[winner_name] += 1
    else:
        leaders[winner_name] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    with open(filename, 'w', encoding='utf-8') as fout:
        json.dump(leaders, fout)


def log(msg):
    directory: str = os.path.dirname(__file__)
    filename: str = os.path.join(directory, 'rps.log')

    with open(filename, 'a', encoding='utf-8') as fout:
        fout.write(f"[{datetime.datetime.now().date().isoformat()}] ")
        fout.write(msg)
        fout.write('\n')


if __name__ == '__main__':
    main()
