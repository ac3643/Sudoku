#!/usr/bin/env python
#coding:utf-8

import sys
import time
import statistics
import collections



""" Global variables """
ROW = "ABCDEFGHI"
COL = "123456789"

#set(A1-C3)
board1 = set(ROW[r]+COL[c] for r in range(3) for c in range(3))
        
#set(D1-F3)
board2 = set(ROW[r]+COL[c] for r in range(3,6) for c in range(3))

#set(G1-I3)
board3 = set(ROW[r]+COL[c] for r in range(6,9) for c in range(3))

#set(A4-C6)
board4 = set(ROW[r]+COL[c] for r in range(3) for c in range(3,6))
       
#set(D4-F6)
board5 = set(ROW[r]+COL[c] for r in range(3,6) for c in range(3,6))

#set(G4-I6)
board6 = set(ROW[r]+COL[c] for r in range(6,9) for c in range(3,6))
        
#set(A7-C9)
board7 = set(ROW[r]+COL[c] for r in range(3) for c in range(6,9))
        
#set(D7-F9)
board8 = set(ROW[r]+COL[c] for r in range(3,6) for c in range(6,9))
        
#set(A7-C9)
board9 = set(ROW[r]+COL[c] for r in range(6,9) for c in range(6,9))

BLOCKS = {1: board1, 2: board2, 3: board3, 4: board4, 5: board5, 6: board6, 7: board7, 8: board8, 9: board9}


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def select_unassigned(board):
    
    """select using MRV heuristic"""
    
    var = {}
    
    for k,v in board.items():
        if v == 0:
            var[k] = {1,2,3,4,5,6,7,8,9}
            
    dic_row = {}
    dic_col = {}
    dic_block = {}
    for i in ROW:
        elements = set()
        for k,v in board.items():
            if (i == k[0]):
                elements.add(v)
            dic_row[i] = elements
    
    for i in COL:
        elements = set()
        for k,v in board.items():
            if (i == k[1]):
                elements.add(v)
            dic_col[i] = elements
     
    #problem happening here... 
    for i,j in BLOCKS.items():
        elements = set()
        for k,v in board.items():
            for x in j:
                if (k == x):
                    elements.add(v)
                dic_block[i] = elements
     

    for i,j in var.items():
        #check_row:
        for k,v in dic_row.items():
            if (i[0] == k):
                var[i] = var[i] - dic_row[k]
        #check col 
    #for i,j in var.items():
        for k,v in dic_col.items():
            if (i[1] == k):
                var[i] = var[i] - dic_col[k]
                
    #for i,j in var.items():       
        #check block
        if (i[0] == 'A') or (i[0] == 'B') or (i[0] == 'C'):
            #group 1,4,7
            #group1
            for x in range(1,4):
                if i[1] == str(x):
                    #i belongs to group 1:
                    var[i] = var[i] - dic_block[1]
                    #break
            for x in range(4,7):
                if i[1] == str(x):
                    #i belongs to group 4:
                    var[i] = var[i] - dic_block[4]
                    #break
            for x in range(7,10):
                if i[1] == str(x):
                    #i belongs to group 7:
                    var[i] = var[i] - dic_block[7]
                    #break
        if (i[0] == 'D') or (i[0] == 'E') or (i[0] == 'F'):
            #group 2,5,8
            for x in range(1,4):
                if i[1] == str(x):
                    #i belongs to group 2:
                    var[i] = var[i] - dic_block[2]
                    #break
            for x in range(4,7):
                if i[1] == str(x):
                    #i belongs to group 5:
                    var[i] = var[i] - dic_block[5]
                    #break
            for x in range(7,10):
                if i[1] == str(x):
                    #i belongs to group 8:
                    var[i] = var[i] - dic_block[8]
                    #break
        
        if (i[0] == 'G') or (i[0] == 'H') or (i[0] == 'I'):
            #group 3,6,9
            #group1
            for x in range(1,4):
                if i[1] == str(x):
                    #i belongs to group 3:
                    var[i] = var[i] - dic_block[3]
                    #break
            for x in range(4,7):
                if i[1] == str(x):
                    #i belongs to group 6:
                    var[i] = var[i] - dic_block[6]
                    #break
            for x in range(7,10):
                if i[1] == str(x):
                    #i belongs to group 9:
                    var[i] = var[i] - dic_block[9]
                    #break
                   
    min_val = min(len(var[v]) for v in var)

    ans = [k for k, v in var.items() if len(v) == min_val]

   
    return (str(ans[0]), list(var[ans[0]]))

            

def order_domain(var, assignment, board):
    
    """order domain"""
    
    if (len(assignment) <= 1):
        
        return assignment
    
    
    cons_lev = {}
    for i in assignment:
        cons_lev[i] = 0
    
    for v in board.values():
        if v in assignment:
            cons_lev[v] =+ 1
    
    
    cons_lev = {k: v for k, v in sorted(cons_lev.items(), key=lambda item: item[1])}#, reverse = True)}
    
    #get keys in sorted order
    res = [k for k in cons_lev.keys()]
    
    return res

def is_consistent(var, w, board):
    
    """forward checking"""
    
    board2 = board.copy()
    board2[var] = w
    temp = {}
    dic_row = {}
    dic_col = {}
    dic_block = {}
    
    for i in ROW:
        elements = set()
        for k,v in board2.items():
            if (i == k[0]):
                elements.add(v)
            dic_row[i] = elements
    
    for i in COL:
        elements = set()
        for k,v in board2.items():
            if (i == k[1]):
                elements.add(v)
            dic_col[i] = elements
     
   
    for i,j in BLOCKS.items():
        elements = set()
        for k,v in board2.items():
            for x in j:
                if (k == x):
                    elements.add(v)
                dic_block[i] = elements
    
    for k,v in board2.items():
        if (v == 0):
            temp[k] = {1,2,3,4,5,6,7,8,9}
    
    
    for i,j in temp.items():
        #check_row:
        for k,v in dic_row.items():
            if (i[0] == k):
                temp[i] = temp[i] - dic_row[k]
        #check col 
        for k,v in dic_col.items():
            if (i[1] == k):
                temp[i] = temp[i] - dic_col[k]
                
          
        #check block
        if (i[0] == 'A') or (i[0] == 'B') or (i[0] == 'C'):
            #group 1,4,7
            #group1
            for x in range(1,4):
                if i[1] == str(x):
                    #i belongs to group 1:
                    temp[i] = temp[i] - dic_block[1]
                    #break
            for x in range(4,7):
                if i[1] == str(x):
                    #i belongs to group 4:
                    temp[i] = temp[i] - dic_block[4]
                    #break
            for x in range(7,10):
                if i[1] == str(x):
                    #i belongs to group 7:
                    temp[i] = temp[i] - dic_block[7]
                    #break
        if (i[0] == 'D') or (i[0] == 'E') or (i[0] == 'F'):
            #group 2,5,8
            for x in range(1,4):
                if i[1] == str(x):
                    #i belongs to group 2:
                    temp[i] = temp[i] - dic_block[2]
                    #break
            for x in range(4,7):
                if i[1] == str(x):
                    #i belongs to group 5:
                    temp[i] = temp[i] - dic_block[5]
                    #break
            for x in range(7,10):
                if i[1] == str(x):
                    #i belongs to group 8:
                    temp[i] = temp[i] - dic_block[8]
                    #break
        if (i[0] == 'G') or (i[0] == 'H') or (i[0] == 'I'):
            #group 3,6,9
            #group1
            for x in range(1,4):
                if i[1] == str(x):
                    #i belongs to group 3:
                    temp[i] = temp[i] - dic_block[3]
                    #break
            for x in range(4,7):
                if i[1] == str(x):
                    #i belongs to group 6:
                    temp[i] = temp[i] - dic_block[6]
                    #break
            for x in range(7,10):
                if i[1] == str(x):
                    #i belongs to group 9:
                    temp[i] = temp[i] - dic_block[9]
                    #break
    
    
    for v in temp.values():
        if (len(v) == 0):
            return False

    return True
    
    

    

def backtracking(board):
    
    """Takes a board and returns solved board."""
    
    val = 0
    if val not in board.values():
        return board 
    
    var, assignment = select_unassigned(board)

    values = order_domain(var, assignment, board) #returns a []
    #print(board)

    for i in values:
        
        if is_consistent(var, i, board):
            board[var] = i
            result = backtracking(board)
            #returns a board or false 
            if result != False:
                return result
            board[var] = 0
       
    return False
        


if __name__ == '__main__':
    
    
    if len(sys.argv) > 1:
        try:
            sudoku_list = sys.argv[1]
        except:
            print("program only takes 2 args (program file, sudoku puzzle)")
            exit()  
    else:
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()
    
    """
    stats = [] #min, max, mean, standard dev, count
    times = []
    boards_solved = 0
    total_start = time.time()
        
    
    #  Read boards from source.
    src_filename = 'sudokus_start.txt'
    try:
        srcfile = open(src_filename, "r")
        sudoku_list = srcfile.read()
    except:
        print("Error reading the sudoku file %s" % src_filename)
        exit()
    """
    
    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")
   

    #create list to put all times 
    # Solve each board using backtracking
    for line in sudoku_list.split("\n"):
        
        start = time.time()

        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(line[9*r+c])
                  for r in range(9) for c in range(9)}
        

        # Print starting board. TODO: Comment this out when timing runs.
        print_board(board)

        # Solve with backtracking
        solved_board = backtracking(board)
        
        #print(solved_board)
        #print("run: {}".format(end/60))

        # Print solved board. TODO: Comment this out when timing runs.
        print_board(solved_board)

        # Write board to file
        if (solved_board):
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')
            #boards_solved +=1
        else:
            outfile.write("failure")
            outfile.write("\n")
        end = time.time() - start
        #Comment out when timing runs
        print("time: {} minutes".format(end/60))
        #times.append((end/60))
    
    #total_time = time.time() - total_start
    outfile.close()
    
        
    
    """
    #time stuff
    stats.append("Total time: {} minutes".format(total_time/60))
    stats.append("Min time: {} minutes".format(min(times)))
    stats.append("Max time: {} minutes".format(max(times)))
    stats.append("Mean time: {} ".format(statistics.mean(times)))
    stats.append("Standard deviation: {}".format(statistics.stdev(times)))
    stats.append("Number of boards solved: {}".format(boards_solved))
    
    read_me_name = 'README.txt'
    README = open(read_me_name, "w")
    
    for i in stats:
        README.write(i)
        README.write("\n")
    
    README.close()
    
    """
  

    print("Finishing all boards in file.")
    