import random

board = {"top-L": "", "top-M": "", "top-R": "", "mid-L": "", "mid-M": "", "mid-R": "", "low-L": "", "low-M": "",
         "low-R": ""}


def draw():
    print(board["top-L"] + " ┃ " + board["top-M"] + " ┃ " + board["top-R"])
    print("------")
    print(board["mid-L"] + " ┃ " + board["mid-M"] + " ┃ " + board["mid-R"])
    print("------")
    print(board["low-L"] + " ┃ " + board["low-M"] + " ┃ " + board["low-R"])


while True:
    if board["low-L"] and board["low-M"] and board["low-R"] == "X": # horizontal
        print("You won!")
        break
    if board["mid-L"] and board["mid-M"] and board["mid-R"] == "X":
        print("You won!")
        break
    if board["top-L"] and board["top-M"] and board["top-R"] == "X":
        print("You won!")
        break
    if board["low-L"] and board["mid-L"] and board["top-L"] == "X": # Vertical
        print("You won!")
        break
    if board["low-M"] and board["mid-M"] and board["top-M"] == "X":
        print("You won!")
        break
    if board["low-R"] and board["mid-R"] and board["top-R"] == "X":
        print("You won!")
        break
    if board["low-L"] and board["mid-M"] and board["top-R"] == "X": # A cross
        print("You won!")
        break
    if board["low-R"] and board["mid-M"] and board["top-L"] == "X":
        print("You won!")
        break

    player = input("Choose your position top-L,top-M,top-R,mid-L,mid-M,mid-R,low-L,low-M,low-R ")
    if player == "top-L":  # Top row
        board["top-L"] = "X"
    elif player == "top-M":
        board["top-M"] = "X"
    elif player == "top-R":
        board["top-R"] = "X"
    elif player == "mid-L":  # Mid row
        board["mid-L"] = "X"
    elif player == "mid-M":
        board["mid-M"] = "X"
    elif player == "mid-R":
        board["mid-R"] = "X"
    elif player == "low-L":  # Low row
        board["low-L"] = "X"
    elif player == "low-M":
        board["low-M"] = "X"
    elif player == "low-R":
        board["low-R"] = "X"
    draw()
