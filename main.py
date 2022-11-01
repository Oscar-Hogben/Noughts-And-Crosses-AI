# UNDEFEATABLE NOUGHTS AND CROSSES AI


# IMPORTS

from clear import clear

green = "\033[1;32;12m"
red = "\033[0;31;12m"
orange = "\033[0;33;12m"
white = "\033[0;37;12m"
blank = "\033[0;37;12m"


# ARRAYS

WIN_CONDITIONS = [
    [
        1,1,1,
        0,0,0,
        0,0,0
    ],

    [
        1,0,0,
        0,1,0,
        0,0,1
    ]
]

tactics = [

    [[
         0,-1,-1,
        -1, 1,-1,
        -1,-1,-1
    ],
    [
        -1,-1,-1,
        -1,-1,-1,
        -1,-1, 0
    ]],

    [[
        0,1,-1,
        -1,-1,-1,
        -1,-1,-1
    ],
    [
        -1,-1,-1,
        -1,0,-1,
        -1,-1,-1
    ]],

    [[
        0,1,-1,
        -1,0,-1,
        -1,-1,1
    ],
    [
        -1,-1,-1,
        -1,-1,-1,
        0,-1,-1
    ]],

    [[
        0,-1,-1,
        -1,-1,1,
        -1,-1,-1
    ],
    [
        -1,-1,-1,
        -1,0,-1,
        -1,-1,-1
    ]],

    [[
        0,-1,-1,
        -1,-1,-1,
        -1,1,-1
    ],
    [
        -1,-1,-1,
        -1,0,-1,
        -1,-1,-1
    ]],

    [[
        0,-1,-1,
        1,-1,-1,
        -1,-1,-1
    ],
    [
        -1,-1,-1,
        -1,0,-1,
        -1,-1,-1
    ]],

    [[
        0,-1,-1,
        1,0,-1,
        -1,-1,1
    ],
    [
        -1,-1,0,
        -1,-1,-1,
        -1,-1,-1
    ]],

    [[
        0,-1,1,
        -1,-1,-1,
        -1,-1,-1
    ],
    [
        -1,-1,-1,
        -1,-1,-1,
        -1,-1,0
    ]],

    [[
        0,-1,-1,
        -1,-1,-1,
        -1,-1,1
    ],
    [
        -1,-1,-1,
        -1,-1,-1,
        0,-1,-1
    ]],

    [[
        0,-1,-1,
        1,-1,-1,
        0,-1,1
    ],
    [
        -1,-1,0,
        -1,-1,-1,
        -1,-1,-1
    ]],

    [[
        0,-1,-1,
        -1,-1,-1,
        1,-1,-1
    ],
    [
        -1,-1,-1,
        -1,-1,-1,
        -1,-1,0
    ]],

    [[
        1,-1,-1,
        -1,-1,-1,
        -1,-1,-1
    ],
    [
        -1,-1,-1,
        -1,0,-1,
        -1,-1,-1
    ]],
    
    [[
        1,-1,-1,
        -1,0,1,
        -1,-1,-1
    ],
    [
        -1,-1,0,
        -1,-1,-1,
        -1,-1,-1
    ]],

    [[
        1,1,0,
        0,0,1,
        1,-1,-1
    ],
    [
        -1,-1,-1,
        -1,-1,-1,
        -1,0,-1
    ]],

    [[
        1,-1,-1,
        -1,0,-1,
        -1,-1,1
    ],
    [
        -1,0,-1,
        -1,-1,-1,
        -1,-1,-1
    ]],

    [[
        1,-1.-1,
        -1,0,-1,
        -1,1,-1
    ],
    [
        -1,-1,-1,
        -1,-1,-1,
        0,-1,-1
    ]],

    [[
        1,0,1,
        1,0,-1,
        0,1,-1
    ],
    [
        -1,-1,-1,
        -1,-1,0,
        -1,-1,-1
    ]],

    [[
        -1,1,-1,
        -1,-1,-1,
        -1,-1,-1
    ],
    [
        -1,-1,-1,
        -1,0,-1,
        -1,-1,-1
    ]],

    [[
        -1,1,-1,
        -1,-1,-1,
        -1,-1,-1
    ],
    [
        -1,-1,-1,
        -1,0,-1,
        -1,-1,-1
    ]],

    [[
        -1,1,-1,
        -1,0,1,
        -1,-1,-1
    ],
    [
        -1,-1,0,
        -1,-1,-1,
        -1,-1,-1
    ]],

    [[
        -1,1,-1,
        -1,0,-1,
        -1,-1,1
    ],
    [
       -1,-1,0,
       -1,-1,-1,
       -1,-1,-1 
    ]],

    [[
        -1,1,-1,
        -1,0,-1
        -1,1,-1
    ],
    [
        -1,-1,0,
        -1,-1,-1,
        -1,-1,-1
    ]],

    [[
        -1,1,-1,
        -1,0,-1,
        1,-1,-1
    ],
    [
        0,-1,-1,
        -1,-1,-1,
        -1,-1,-1
    ]],

    [[
        -1,1,-1,
        1,0,-1,
        -1,-1,-1
    ],
    [
        0,-1,-1,
        -1,-1,-1,
        -1,-1,-1
    ]],

    [[
        -1,-1,-1,
        -1,1,-1,
        -1,-1,-1
    ],
    [
        0,-1,-1,
        -1,-1,-1,
        -1,-1,-1
    ]],

    [[
        0,-1,-1,
        -1,1,-1,
        -1,-1,1
    ],
    [
        -1,-1,0,
        -1,-1,-1,
        -1,-1,-1
    ]]
]

Player_Board = [
    -1,-1,-1,
    -1,-1,-1,
    -1,-1,-1
]


# SUBROUTINES

def printBoard(board):
    board = board.copy()

    print(f"""
        A    {board[0]} | {board[1]} | {board[2]}
            -----------
        B    {board[3]} | {board[4]} | {board[5]}
            -----------
        C    {board[6]} | {board[7]} | {board[8]}

             A   B   C
    """.replace("0","O").replace("-1", " ").replace("1","X"))
    
def win(player):

    if player == 0:
        print(f"{red}AI Wins!{blank}")
        exit()
    elif player == 1:
        print(f"{green}Player Wins!{blank}")

        file = open("code.hidden", "r")
        print(f"Amazon gift voucher: {file.read()}")
        file.close()

        exit()
    elif player == -1:
        print(f"{orange}Draw!{blank}")
        exit()

def rotate(board):
    origonal = board.copy()

    board[0] = origonal[6]
    board[1] = origonal[3]
    board[2] = origonal[0]
    
    board[3] = origonal[7]
    board[4] = origonal[4]
    board[5] = origonal[1]

    board[6] = origonal[8]
    board[7] = origonal[5]
    board[8] = origonal[2]

    return board.copy()

def checkWin(board):
    tempWin1 = WIN_CONDITIONS[0].copy()
    tempWin2 = WIN_CONDITIONS[1].copy()

    if board.count(-1) == 0:
        printBoard(board)
        win(-1)

    for i in range(4):

        winTotal = 0
        for place in range(9):
            value = tempWin1[place]
            if board[place] == 1 and value == 1:
                winTotal += 1
        if winTotal == 3:
            printBoard(board)
            win(1)
        
        winTotal = 0
        for place in range(9):
            value = tempWin2[place]
            if board[place] == 1 and value == 1:
                winTotal += 1
        if winTotal == 3:
            printBoard(board)
            win(1)

        
        winTotal = 0
        for place in range(9):
            value = tempWin1[place]
            if board[place] == 0 and value == 1:
                winTotal += 1
        if winTotal == 3:
            printBoard(board)
            win(0)
        
        winTotal = 0
        for place in range(9):
            value = tempWin2[place]
            if board[place] == 0 and value == 1:
                winTotal += 1
        if winTotal == 3:
            printBoard(board)
            win(0)

        

        tempWin1 = rotate(tempWin1)
        tempWin2 = rotate(tempWin2)

def place(piece, pos, board):

    board = board.copy()

    x = int(pos[0])
    y = int(pos[1])

    board[y*3+x] = piece

    return board.copy()

def ai_move(board):
    done = False

    board = board.copy()

    # Check if AI can win

    for i in range(4):

        if not done and [board[0],board[1],board[2]].count(0) == 2 and [board[0],board[1],board[2]].count(-1) == 1:

            for i in range(3):
                square = board[i]

                if square == -1:
                    board[i] = 0
                    done = True
                            
        if not done and [board[0],board[4],board[8]].count(0) == 2 and [board[0],board[4],board[8]].count(-1) == 1:

            for i in range(0,8,4):

                square = board[i]

                if square == -1:
                    board[i] = 0
                    done = True

        if not done and [board[1],board[4],board[7]].count(0) == 2 and [board[1],board[4],board[7]].count(-1) == 1:

            for i in range(1,7,3):

                square = board[i]

                if square == -1:
                    board[i] = 0
                    done = True


        board = rotate(board)

    # Check if Player can win

    for i in range(4):

        if not done and [board[0],board[1],board[2]].count(1) == 2 and [board[0],board[1],board[2]].count(-1) == 1:

            for i in range(3):
                square = board[i]

                if square == -1:
                    board[i] = 0
                    done = True
        
        if not done and [board[0],board[4],board[8]].count(1) == 2 and [board[0],board[4],board[8]].count(-1) == 1:

            for i in range(0,8,4):

                square = board[i]

                if square == -1:
                    board[i] = 0
                    done = True

        if not done and [board[1],board[4],board[7]].count(1) == 2 and [board[1],board[4],board[7]].count(-1) == 1:

            for i in range(1,7,3):

                square = board[i]

                if square == -1:
                    board[i] = 0
                    done = True

        board = rotate(board)

    # Check if nothing is on the board

    if not done and board.count(-1) == 9:
        board[0] = 0
        done = True

    # Check Tactics

    for i in range(4):
        for tactic in tactics:
            if board == tactic[0] and not done:
                for v in range(9):
                    if tactic[1][v] == 0:
                        board[v] = 0
                        done = True

        board = rotate(board)
    
    for i in range(8):
        if board[i] == -1 and not done:
            board[i] = 0
            done = True
    
    if not done:
        exit("Exited with error code: 001")

    return board


# MAIN PROGRAM

clear()

print(f"{green}Win to get an Amazon gift code!{blank}\n")

print("Would you like to go first? (y/n): ")
start = input()

clear()

if start == "y":

    while True:
        print("Enter the co-ordinates of where you would like to go (XY): ")
        printBoard(Player_Board)

        coords = input().replace(" ","").upper()
        coords = coords.replace("A","0").replace("B", "1").replace("C", "2")

        try:
            int(coords)

            if Player_Board[int(coords[1])*3 + int(coords[0])] == -1 and (coords.count("0") + coords.count("1") + coords.count("2") == 2):
                Player_Board = place(1, coords, Player_Board)
                break
            else:
                clear()
                print("That is not valid!")
        except:
            clear()
            print("That is not valid!")

while True:

    Player_Board = ai_move(Player_Board)

    clear()

    checkWin(Player_Board)

    while True:
        print("Enter the co-ordinates of where you would like to go (XY): ")
        printBoard(Player_Board)

        coords = input().replace(" ","").upper()
        coords = coords.replace("A","0").replace("B", "1").replace("C", "2")

        try:
            int(coords)

            if Player_Board[int(coords[1])*3 + int(coords[0])] == -1 and (coords.count("0") + coords.count("1") + coords.count("2") == 2):
                Player_Board = place(1, coords, Player_Board)
                break
            else:
                clear()
                print("That is not valid!")
        except:
            clear()
            print("That is not valid!")

    clear()

    checkWin(Player_Board)
