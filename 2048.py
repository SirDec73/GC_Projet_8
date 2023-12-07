import random
import os
from Test_Varibles import*

# Create list for restart key autorisation
autorisation_key_restart:str = ['Y','YES','N','NO']

# Create a grid for the game
Grid: list[list[int]] = \
    [
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]
    ]


# Display Function
def printGrid(grid: list[list[int]], n):
    os.system('cls')
    for i in range(len(grid)):
        print("+---" * n +"+")
        for j in range(len(grid[i])):
            print("| " + str(grid[i][j]) + " ", end="")
        print("|")    
    print("+---" * n +"+")


# Reverse the grid (Top to Bottom)
def reverseGridUpDown():
    reserve = Grid[0]
    Grid[0] = Grid[3]
    Grid[3] = reserve
    reserve = Grid[1]
    Grid[1] = Grid[2]
    Grid[2] = reserve


# Reset the grid
def Initiat_Grid():
    global Grid
    Grid = [[0 for _ in range(4)]for _ in range(4)]


# Check if 2048 is make
def Check2048():
    for elem in Grid:
        if 2048 in elem:
            return True,True
    return False,False


# Function for move the grid in 1 direction
def Move_grid(control):
    
    # Check the grid move min 1 time
    make_move:bool = False

    # Move the grid Up or Down
    if control == 'Up' or control == 'Down':
        if control == 'Down':
            reverseGridUpDown()

        # for each col of the grid
        for j in range(0,4):

            # for each row of the grid
            for i in range(0,4):
                if Grid[i][j] != 0 : 
                    reserve = Grid[i][j]

                    # Index des num d'une colonne
                    for k in range(0,i+1):
                        
                        if Grid[k][j] == 0:
                            try:
                                Grid[k][j] = reserve
                                Grid[i][j] = 0
                                make_move = True
                                break
                            except IndexError:
                                pass
        if control == 'Down':
            reverseGridUpDown()

    # Move the grid Left
    elif control == 'Left':

        # for each row of the grid
        for counter,j in enumerate(Grid):

            # for each number of the row
            for i in range(0,4):
                if j[i] != 0 :

                    # for each column of the others in the grid
                    for k in range(0,i):
                        try:
                            if Grid[counter][k]== 0:
                                Grid[counter][k] = j[i]
                                j[i] = 0
                                make_move = True
                        except IndexError:
                            print('error') 
                    

    # Move the grid Right
    elif control == 'Right':
        
        #for each row of the grid
        for counter,j in enumerate(Grid):

            # for each number of the row
            for i in range(0,4):
                if j[3-i] != 0 :
                    
                    # for each column of the others in the grid
                    for k in range(0,i):
                        try:
                            if Grid[counter][3-k]== 0:
                                Grid[counter][3-k] = j[3-i]
                                j[3-i] = 0
                                make_move = True
                        except IndexError:
                            print('error')                
    return make_move

def Fusion(control,Nb_in_Grid):
    make_fusion:bool = False
    if control == 'Left':

        #index row
        for i in range(0,4):

            #index col
            for j in range(0,4):
                try :
                    if Grid[i][j] == Grid[i][j+1] and Grid[i][j] >0:
                        Grid[i][j] *= 2
                        Grid[i][j+1] = 0
                        Nb_in_Grid = Nb_in_Grid - 1
                        make_fusion = True
                except IndexError:
                    pass
    
    elif (control == 'Right'):

        #index row
        for i in range(0,4):

            #index col
            for j in range(4,0,-1):
                try :
                    if Grid[i][j] == Grid[i][j-1] and j-1 >= 0 and Grid[i][j] != 0:
                        Grid[i][j-1] = 0
                        Grid[i][j] *= 2
                        Nb_in_Grid = Nb_in_Grid - 1
                        make_fusion = True

                except IndexError:
                    pass

    #Fusion vers le haut
    elif control == 'Up' or control == 'Down':
        if control == 'Down':
            reverseGridUpDown()

        # index row
        for i in range(0,4) :

            # index col
            for j in range(0, 4) :
                try:
                    if Grid[i][j] == Grid[i-1][j] and i-1 >= 0 and Grid[i][j] != 0:
                        Grid[i-1][j] *= 2
                        Grid[i][j] = 0
                        Nb_in_Grid = Nb_in_Grid - 1
                        make_fusion = True
                except IndexError:
                    pass

        if control == 'Down':
            reverseGridUpDown()
            
    return Nb_in_Grid,make_fusion

# Function for check if you can move at the end of the game
def Check_Possible_Move_Fusion():
    for i in range(0,4):
        for j in range(0,4):

            # move on left or right ?
            try :
                if Grid[i][j] == Grid[i][j+1]:
                    return True
            except IndexError:
                    pass
            
            # move on Top or Bottom ?
            try :
                if Grid[i][j] == Grid[i+1][j]:
                    return True
            except IndexError:
                    pass
            
    return False


def Game():
    END: bool = False
    Nb_in_Grid = 0
    make_move=True
    make_fusion:bool = True

    while not END :

        Place_A_Number:bool = False

        # Take a random position for increase it by 2 or 4
        while not Place_A_Number and (make_move or make_fusion):
            Random_row:int = random.randint(0,3)
            Random_col:int = random.randint(0,3)
            Random_num:int = random.randint(1,6)
            if Random_num == 1:
                Random_num = 4
            else : Random_num = 2

            if Grid[Random_row][Random_col] == 0:
                Grid[Random_row][Random_col] = Random_num
                Place_A_Number = True
                Nb_in_Grid = Nb_in_Grid + 1
            if not Check_Possible_Move_Fusion() and Nb_in_Grid >= 16:
                Possible_move = False
                break
            else:
                Possible_move = True
            if Possible_move and Nb_in_Grid == 16:
                break

        printGrid(Grid, 4)

        if Possible_move :
            # Ask where the user want to move the grid
            control:str = Ask_Input("Up -> 'Z' | Left -> 'Q' | Down -> 'S' | Right -> 'D'  : ", ['Z','Q','S','D'] , ['Up','Left','Down','Right']) 

            # Move the grid | Fusion what he can | Move the grid again
            make_move = Move_grid(control)
            Nb_in_Grid,make_fusion = Fusion(control,Nb_in_Grid)
            Move_grid(control)
            END,Win = Check2048()
        else:
            END,Win = True,False

        printGrid(Grid, 4)

        # End game
        if END == True:
            if Win == True:
                print('GG WP !')

            if Win == False:
                print('LOOSER !')

            # Restart the game
            Restart:str = Ask_Input("Retry --> 'Y' / 'YES' | STOP --> 'N' / 'NO' : ",autorisation_key_restart)
            if Restart.upper() == autorisation_key_restart[0] or Restart.upper() == autorisation_key_restart[1]:
                print('Game Restarted !')
                END = False
                Win = False
                make_move=True
                make_fusion:bool = True
                Nb_in_Grid:int = 0
                Initiat_Grid()
            else:
                print('See you next time')
    
Game()
