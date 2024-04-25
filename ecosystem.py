import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

#FINISH ADDING BORDER COMBINATION OPTIONS FOR ALL OF THESE
#FINISH ADDING BREEDING BEHAVIOR
#9xx9 Upper Right Corner
#x9x9 Lower Right Corner
#9x9x Upper Left Corner
#x99x Lower Left Corner

#9xxx Upper Border
#x9xx Lower Border
#xx9x Left Border
#xxx9 Right Border

prey_move_left_options=[9209,#upper right corner, predator below
                        2909,#lower right corner, predator above
                        2202,#surrounded by preds except for left
                        2209,#right border, preds above and below
                        9202,#top border, preds below and right
                        2902,#bottom border, preds above and right
                        1102,
                        1201,
                        1202,
                        2101,
                        2102,
                        2201]
prey_move_right_options=[9290, #upper left corner, predator below
                         2990, #lower left corner, predator above
                         2220, #surrounded by preds except for right
                         2290, #left border, preds above and below
                         9220, #top border, preds below and left
                         2920, #bottom border, preds above and left
                         1120,
                         1210,
                         1220,
                         2110,
                         2120,
                         2210] 
prey_move_down_options=[1012,
                        1021,
                        1022,
                        2011,
                        2012,
                        2021,
                        2022]
prey_move_up_options=[112,
                      121,
                      122,
                      211,
                      212,
                      221,
                      222]
prey_move_up_down_left_options=[2]
prey_move_up_down_options=[12,21,22]
prey_move_up_down_right_options=[20]
prey_move_up_left_options=[102,201,202]
prey_move_up_right_options=[120,210,220]
prey_move_up_left_right_options=[200]
prey_move_down_left_options=[1002,2001,2002]
prey_move_down_right_options=[1020,2010,2020]
prey_move_left_right_options=[1100,1200,2100,2200]
prey_move_down_left_right_options=[2000]


pred_move_left_options = [10,12,210,212,2010,2012,2202,2210,2212,9019,9209,9219,919,2909,2919,9010,9012,9202,9210,9212,910,912,2902,2910,2912,19,219,2019,2209,2219]
pred_move_right_options = [1,21,201,221,2001,2021,2201,2220,2221,9091,9290,9291,991,2990,2991,9001,9021,9201,9220,9221,901,921,2901,2920,2921,91,291,2091,2290,2291,]
pred_move_down_options = [100,102,120,122,2022,2100,2102,2120,2122,9029,9109,9129,9092,9190,9192,9022,9100,9102,9120,9122,190,192,2092,2190,2192,109,129,2029,2109,2129]
pred_move_up_options = [222,1000,1002,1020,1022,1200,1202,1220,1222,929,1909,1929,992,1990,1992,922,1900,1902,1920,1922,292,1090,1092,1290,1292,229,1009,1029,1209,1229]
pred_move_up_down_left_options=[2,1110,1112,9,1119,]
pred_move_up_down_options=[22,1100,1102,1120,1122,92,1190,1192,29,1109,1129]
pred_move_up_down_right_options=[20,1101,1121,90,1191]
pred_move_up_left_options=[202,1010,1012,1210,1212,909,1919,902,1910,1912,209,1019,1219]
pred_move_up_right_options=[220,1001,1021,1201,1221,990,1991,920,1901,1921,290,1091,1291,]
pred_move_up_left_right_options=[200,1011,1211,900,1911]
pred_move_down_left_options=[110,112,2002,2110,2112,9009,9119,9002,9110,9112,119,2009,2119]
pred_move_down_right_options=[101,121,2020,2101,2121,9090,9191,9020,9101,9121,191,2090,2191,]
pred_move_left_right_options=[11,211,2011,2200,2211,9011,9200,9211,911,2900,2911,]
pred_move_down_left_right_options=[111,2000,2111,9000,9111]


class Prey:
    def __init__(self):
        self.reproduce = False
        self.value = 1
        self.location = (0,0)
        self.move = True

class Predator:
    def __init__(self):
        self.reproduce = False
        self.value = 2
        self.location = (0,0)
        self.move = True

def move_up(board,cell):
    cell_row,cell_col = cell.location
    #print(f"Moving cell up from {cell.location} to {cell_row-1} {cell_col}")
    board[cell_row-1][cell_col] = cell
    board[cell_row][cell_col] = None
    cell.location = (cell_row-1, cell_col)
    cell.move = False
def move_down(board,cell):
    cell_row,cell_col = cell.location
    #print(f"Moving cell down from {cell.location} to {cell_row+1} {cell_col}")
    board[cell_row+1][cell_col] = cell
    board[cell_row][cell_col] = None
    cell.location = (cell_row+1, cell_col)
    cell.move = False
def move_right(board,cell):
    cell_row,cell_col = cell.location
    #print(f"Moving cell right from {cell.location} to {cell_row} {cell_col+1}")
    board[cell_row][cell_col+1] = cell
    board[cell_row][cell_col] = None
    cell.location = (cell_row, cell_col+1)
    cell.move = False
def move_left(board,cell):
    cell_row,cell_col = cell.location
    #print(f"Moving cell left from {cell.location} to {cell_row} {cell_col-1}")
    board[cell_row][cell_col-1] = cell
    board[cell_row][cell_col] = None
    cell.location = (cell_row, cell_col-1)
    cell.move = False

def move_up_down_left(board,cell):
    random_number = random.randint(0, 2)
    if random_number == 0:
        move_up(board,cell)
    elif random_number == 1:
        move_down(board,cell)
    elif random_number == 2:
        move_left(board,cell)
def move_up_down(board,cell):
    random_number = random.randint(0, 1)
    if random_number == 0:
        move_up(board,cell)
    elif random_number == 1:
        move_down(board,cell)
def move_up_down_right(board,cell):
    random_number = random.randint(0, 2)
    if random_number == 0:
        move_up(board,cell)
    elif random_number == 1:
        move_down(board,cell)
    elif random_number == 2:
        move_right(board,cell)
def move_up_left(board,cell):
    random_number = random.randint(0,1)
    if random_number == 0:
        move_up(board,cell)
    elif random_number == 1:
        move_left(board,cell)
def move_up_right(board,cell):
    random_number = random.randint(0, 1)
    if random_number == 0:
        move_up(board,cell)
    elif random_number == 1:
        move_right(board,cell)
def move_up_left_right(board,cell):
    random_number = random.randint(0, 2)
    if random_number == 0:
        move_up(board,cell)
    elif random_number == 1:
        move_left(board,cell)
    elif random_number == 2:
        move_right(board,cell)
def move_down_left(board,cell):
    random_number = random.randint(0, 1)
    if random_number == 0:
        move_down(board,cell)
    elif random_number == 1:
        move_left(board,cell)
def move_down_right(board,cell):
    random_number = random.randint(0, 1)
    if random_number == 0:
        move_down(board,cell)
    elif random_number == 1:
        move_right(board,cell)
def move_left_right(board,cell):
    random_number = random.randint(0, 1)
    if random_number == 0:
        move_left(board,cell)
    elif random_number == 1:
        move_right(board,cell)
def move_down_left_right(board,cell):
    random_number = random.randint(0, 2)
    if random_number == 0:
        move_down(board,cell)
    elif random_number == 1:
        move_left(board,cell)
    elif random_number == 2:
        move_right(board,cell)
def move_random(board,cell):
    random_number = random.randint(0, 3)
    if random_number == 0:
        move_up(board,cell)
    elif random_number == 1:
        move_down(board,cell)
    elif random_number == 2:
        move_left(board,cell)
    elif random_number == 3:
        move_right(board,cell)

def create_empty_board(rows, columns):
    print("Creating empty board...\n")
    board = [[None for _ in range(columns)] for _ in range(rows)]
    return board

def populate_board(board, prey_density, predator_density):
    print("Populating board...\n")
    num_rows = len(board)
    num_cols = len(board[0])
    num_prey = int(num_rows * num_cols * prey_density)
    num_predators = int(num_rows * num_cols * predator_density)
    #Populate prey
    for _ in range(num_prey):
        row = random.randint(0, num_rows - 1)
        col = random.randint(0, num_cols - 1)
        if board[row][col] is None:
            board[row][col] = Prey()
            board[row][col].location = (row, col)
    #Populate predators
    for _ in range(num_predators):
        row = random.randint(0, num_rows - 1)
        col = random.randint(0, num_cols - 1)
        if board[row][col] is None:
            board[row][col] = Predator()
            board[row][col].location = (row, col)
    return

def visualize_board(board, filename = None):
    print("\nVisualizing board...")
    empty_color = 'white'
    prey_color = 'green'
    predator_color = 'red'
    cmap = ListedColormap([empty_color, prey_color, predator_color])

    #Convert to a numpy array for plotting
    board_array = np.zeros_like(board, dtype=int)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if isinstance(board[i][j], Prey):
                board_array[i][j] = board[i][j].value
            elif isinstance(board[i][j], Predator):
                board_array[i][j] = board[i][j].value

   #Plot
    plt.figure(figsize=(8, 6))
    plt.imshow(board_array, cmap=cmap, interpolation='nearest')
    cbar = plt.colorbar(ticks=[0, 1, 2])
    cbar.set_ticklabels(['Empty', 'Prey', 'Predator'])
    plt.title('Cellular Automata Board')
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.grid(False)
    if filename:
        plt.savefig(filename) #Save the figure to a file
        plt.close() #Close the figure to free up memory
    else:
        plt.show() #Show the plot if no filename is specified

def get_neighborhood_option(board, cell):
    neighborhood_checklist = [9,9,9,9] #[up,down,left,right]
    cell_row,cell_col = cell.location
    rows = len(board)-1
    cols = len(board[0])-1
        
    #check if cell is on upper border
    if cell.location[0] == 0:
        #Cell on top border
        neighborhood_checklist[0] = 9
    elif isinstance(board[cell_row-1][cell_col],Predator):
        #print("Predator above cell")
        neighborhood_checklist[0] = 2
    elif isinstance(board[cell_row-1][cell_col],Prey):
        #print("Prey above cell")
        neighborhood_checklist[0] = 1
    else:
        neighborhood_checklist[0] = 0

    #check if cell is on bottom border
    if cell.location[0] == rows:
        #print("Cell on bottom border")
        neighborhood_checklist[1] = 9
    elif isinstance(board[cell_row+1][cell_col],Predator):
        #print("Predator below cell")
        neighborhood_checklist[1] = 2
    elif isinstance(board[cell_row+1][cell_col],Prey):
        #print("Prey below cell")
        neighborhood_checklist[1] = 1
    else:
        neighborhood_checklist[1] = 0

    #check if cell is on left border
    if cell.location[1] == 0:
        #print("Cell on left border")
        neighborhood_checklist[2] = 9
    elif isinstance(board[cell_row][cell_col-1],Predator):
        #print("Predator left of cell")
        neighborhood_checklist[2] = 2
    elif isinstance(board[cell_row][cell_col-1],Prey):
        #print("Prey left of cell")
        neighborhood_checklist[2] = 1
    else:
        neighborhood_checklist[2] = 0

    #check if cell is on right border
    if cell.location[1] == cols:
        #print("Cell on right border")
        neighborhood_checklist[3] = 9
    elif isinstance(board[cell_row][cell_col+1],Predator):
        #print("Predator right of cell")
        neighborhood_checklist[3] = 2
    elif isinstance(board[cell_row][cell_col+1],Prey):
        #print("Prey right of cell")
        neighborhood_checklist[3] = 1
    else:
        neighborhood_checklist[3] = 0

    return neighborhood_checklist

def update_cell(board,cell,option):
    #[up,down,left,right]
    #0 = open, 1 = Prey, 2 = Predator, 9 = border
    cell_row,cell_col = cell.location
    option_str = ''.join(map(str, option))
    option_int = int(option_str)
    print(f"CELL: {cell}, OPTION: {option_int}")
    #if cell has already moved, dont move it
    if cell.move == False:
        print("     - CELL ALREADY MOVED, SKIPPING")
        return
    if(isinstance(cell, Predator)): #update predator based on option
        if(option_int == 0 or option_int == 1111): #no neighbors or surrounded by prey, move randomly
            move_random(board,cell)
        elif option_int in pred_move_left_options: #if reason to move left
            move_left(board,cell)
        elif option_int in pred_move_right_options: #if reason to move right
            move_right(board,cell)
        elif option_int in pred_move_down_options: #if reason to move down
            move_down(board,cell)
        elif option_int in pred_move_up_options: #if reason to move up
            move_up(board,cell)
        #elif all other predator_move_options
        elif option_int in pred_move_up_down_left_options:
            move_up_down_left(board,cell)
        elif option_int in pred_move_up_down_options:
            move_up_down(board,cell)
        elif option_int in pred_move_up_down_right_options:
            move_up_down_right(board,cell)
        elif option_int in pred_move_up_left_options:
            move_up_left(board,cell)
        elif option_int in pred_move_up_right_options:
            move_up_right(board,cell)
        elif option_int in pred_move_up_left_right_options:
            move_up_left_right(board,cell)
        elif option_int in pred_move_down_left_options:
            move_down_left(board,cell)
        elif option_int in pred_move_down_right_options:
            move_down_right(board,cell)
        elif option_int in pred_move_left_right_options:
            move_left_right(board,cell)
        elif option_int in pred_move_down_left_right_options:
            move_down_left_right(board,cell)
        
        
    elif(isinstance(cell, Prey)): #update prey based on option
        if(option_int == 0): #no neighbors, move randomly
            move_random(board,cell)
        elif option_int in prey_move_left_options: #if reason to move left
            move_left(board,cell)
        elif option_int in prey_move_right_options: #if reason to move right
            move_right(board,cell)
        elif option_int in prey_move_down_options:#if reason to move down
            move_down(board,cell)
        elif option_int in prey_move_up_options:#if reason to move up
            move_up(board,cell)
        #elif all other prey_move_options
        elif option_int in prey_move_up_down_left_options:
            move_up_down_left(board,cell)
        elif option_int in prey_move_up_down_options:
            move_up_down(board,cell)
        elif option_int in prey_move_up_down_right_options:
            move_up_down_right(board,cell)
        elif option_int in prey_move_up_left_options:
            move_up_left(board,cell)
        elif option_int in prey_move_up_right_options:
            move_up_right(board,cell)
        elif option_int in prey_move_up_left_right_options:
            move_up_left_right(board,cell)
        elif option_int in prey_move_down_left_options:
            move_down_left(board,cell)
        elif option_int in prey_move_down_right_options:
            move_down_right(board,cell)
        elif option_int in prey_move_left_right_options:
            move_left_right(board,cell)
        elif option_int in prey_move_down_left_right_options:
            move_down_left_right(board,cell)

def update_board_state(board):
    for row in board:
        for cell in row:
            if cell != None:
                option = get_neighborhood_option(board, cell)
                update_cell(board,cell,option)
    #reset cell movement flag
    for row in board:
        for cell in row:
            if cell != None:
                cell.move = True
    return