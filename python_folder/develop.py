# # # # # # Activity 1/1 # # # # # 
# Create variable that holds the text “Welcome to Code Nation”. 
# Find the length of the string and save this to a new variable. 
# Create a function that checks if the string length is even; 
# if it is, print the string, the length and an 
# appropriate message in one sentence. Do the same 
# but with a different message if it’s odd. 
# Change the string length so you can test all 
# possible outcomes#
# text = "Welcome to Code Nation"
# lenth = len(text)
# print(text , "contain" , lenth ,"characters, including spaces.")
# # # # # # # Activity 1/2 # # # # # #
def function(string):
    if len(string) % 2 == 0:
        print(f"word: {string} is even")
    else :
        print(f"word: {string} is odd")
function("kalas")
# # # # # # Activity 2 # # # # # #
# Create a list that represents the alphabet:
# alphabet = ["a", "b", "c", "d"...
# Create a for loop to iterate through this and print 
# each letter in order
# Now using input, allow the user to type a number 
# and print the letter it represents in the alphabet.
# Remember how index works - and think about how 
# to structure your code
alphabet = ["A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V",
"W",
"X",
"Y",
"Z"]
def function1():
    num = int(input("Type a number from 1 to 26: "))
    print(alphabet[num - 1])
function1()
# # # # # # Activity 3 # # # # # 
# Remember the noughts and crosses activity? Let’s revisit 
# that and start to improve with our improved knowledge.  
# Create a structure of functions that allow the player to play 
# against the computer - here is a suggestion: 
# Function to start the game, let player choose ‘0’ or ‘X’ 
# Function to print the board & show the player how to 
# choose spaces 
# Function for the player to choose their space 
# Function for the computer to take its turn 
# Function to check the logic of if there’s a win, lose or draw 
# after every turn is taken#
import random
# Lets put all these functions into a class
class Game:
    # Lets set up the game
    def __init__(self, player_one="X", player_two="O"):
        self.player_one = player_one
        self.player_two = player_two
        # Where the game board is stored
        # Using periods instead of spaces so the players can see the possible moves
        self.game_board = [
                            [".", ".", "."],
                            [".", ".", "."],
                            [".", ".", "."]
                          ]
        # This value is to check if the game is still going
        self.running = True
        # Whos turn is it?
        self.active_player = ""
        # The tasks we HAVE to do to make the game work
        self.start_player()
        self.run_game()
    # The function is part of the Game class so we have to pass self into it.
    def start_player(self):
        # Randomly Choose a starting player
        startplayer = random.randint(1,2)
        if startplayer == 1:
            # We declared the string values in the __init__ function
            player = self.player_one
            print("Player One ({}) will start the game.".format(player))
        else:
            startplayer == 2
            player = self.player_two
            print("Player Two ({}) will start the game.".format(player))
        # Set the initial player
        self.active_player = player
    def get_move(self):
        # Seems silly to have them enter the rows and columns one by one
        #row = int(input("Please enter a number between 0 and 2: "))
        #column = int(input("Please enter a number between 0 and 2: "))
        # Show the player whos turn it is
        input_data = input("Player ({}) please choose a Column and a Row: ".format(self.active_player))
        # Default values that aren't in the game, if they arent changed they will be caught
        row = -1
        column = -1
        # Users entry all types of funky data, lets make sure its right
        try:    
            r, c = input_data.split(" ")
            r = int(r)
            c = int(c)
            if r >= 0 and r <= 3:
                row = int(r)
            if c >= 0 and c <= 3:
                column = int(c)
        except:
            print("Enter only two numbers (0, 1, or 2) seperated by a space")
        return row, column
        # This check for the grid should be its own function
        #while grid[row][column] != "":
        #   print("Invalid move.")
        #   row = int(input("Please enter a number between 0 and 2: "))
        #   column = int(input("Please enter a number between 0 and 2: ")) 
    def check_move(self, row, column):
        if row == -1 or column == -1:
            return False
        # If the space is blank return True
        if self.game_board[row][column] == ".":
            return True
        print("{} {} is an invalid move, try again".format(row, column))
        return False
    # Add another function to print out the board for us
    def show_board(self):
        for row in self.game_board:
            row_string = ""
            for cell in row:
                row_string = "{} {} ".format(row_string, cell)
            print(row_string)
    #def mainturn(row, column):
    # Try to avoid using globals. We'll store these in our class
    #global countmove
    #countmove = countmove + 1
    #global symbol
    #grid[row][column] = symbol
    #for y in range(0,(len(grid))):
    #    print(grid[y])
    #if symbol == 'X':
    #    symbol = 'O'
    #elif symbol == 'O':
    #    symbol = 'X'
    #return countmove
    # This is one heck of an if statement. Lets turn it into a function
    # if (grid[0][0] and grid[0][1] and grid[0][2] == symbol) or (grid[1][0] and grid[1][1] and grid[1][2] == symbol) or (grid[2][0] and grid[2][1] and grid[2][2] == symbol) or (grid[0][0] and grid[1][0] and grid[2][0] == symbol) or (grid[0][1] and grid[1][1] and grid[2][1] == symbol)or (grid[0][2] and grid[1][2] and grid[2][2] == symbol)or (grid[0][0] and grid[1][1] and grid[2][2] == symbol) or (grid[2][0] and grid[1][1] and grid[0][2] == symbol):
    def check_win(self, symbol):
        combinations = [
            # horizontal
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            # vertical
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            # crossed
            [(0,0), (1,1), (2,2)],
            [(2,0), (1,1), (0,2)]
            ]
        for coordinates in combinations:
            letters = [self.game_board[x][y] for x, y in coordinates]
            # If all the letters match
            if "." not in letters:
                if len(set(letters)) <= 1:
                    # returns corresponding letter for winner (X/O)
                    print("Well done {}!  You won the game!".format(symbol))
                    self.running = False
                    return True
        return False
    # Lets try another method of checking if the board is full
    #elif countmove == 9:
    #    print("Board Full. Game over.")
    #main program
    def board_full(self):
        for row in self.game_board:
            if "." in row:
                return False
        print("The game is a draw :( ")
        # Stop the game
        self.running = False
        return True
    def run_game(self):
        # While the game is not over
        while self.running != False:
            # Show the player the board
            self.show_board()
            row, column = self.get_move()
            # Is the move valid?
            if self.check_move(row, column):
                self.game_board[row][column] = self.active_player
                # Did they win?
                self.check_win(self.active_player)  
                # Change Players
                if self.active_player == self.player_one:
                    self.active_player = self.player_two
                else:
                    self.active_player = self.player_one
        # Print the winning game board
        self.show_board()
g = Game("X", "O")
    # Handled this in the class
    #grid = [["","",""],["","",""],["","",""]]
    #countmove = 0
    #win = 'false'
    # Turned this code into the show_board function
    #for y in range(0,(len(grid))):
    #print(grid[y])
    #symbol = start_player()