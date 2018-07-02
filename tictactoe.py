# 0 | 1 | 2   
#-----------
# 3 | 4 | 5 
#-----------
# 6 | 7 | 8 



space = " "
empty = "   "
wall = "|"
line = "--------------------"
sec = ['0', '1', '2', '3', '4', '5', '6', '7', '8']



def Board():
        print (space, sec[0], space, wall, space, sec[1], space, wall, space, sec[2], space)
        print (line)
        print (space, sec[3], space, wall, space, sec[4], space, wall, space, sec[5], space)
        print (line)
        print (space, sec[6], space, wall, space, sec[7], space, wall, space, sec[8], space)


#-----------------------------------------------------------------------------------------------

print ('Player 1 is X')
print ('Player 2 is O\n')


x = 0
while( x <= 9 ):

    if x % 2 == 0:
        Board()
        print('Player 1 pick a box')
        y = int(input("enter a number: "))
        sec[y] = 'X'

        # Player 1 victory conditions
        if sec[0] == 'X' and sec[1] == 'X' and sec[2] == 'X':
            print ('Player 1 wins')
            Board()
            break
        elif sec[3] == 'X' and sec[4] == 'X' and sec[5] == 'X':
            print ('Player 1 wins')
            break
        elif sec[6] == 'X' and sec[7] == 'X' and sec[8] == 'X':
            print ('Player 1 wins')
            Board()
            break
        elif sec[0] == 'X' and sec[3] == 'X' and sec[6] == 'X':
            print ('Player 1 wins')
            Board()
            break
        elif sec[1] == 'X' and sec[4] == 'X' and sec[7] == 'X':
            print ('Player 1 wins')
            Board()
            break
        elif sec[2] == 'X' and sec[5] == 'X' and sec[8] == 'X':
            print ('Player 1 wins')
            Board()
            break
        elif sec[0] == 'X' and sec[4] == 'X' and sec[8] == 'X':
            print ('Player 1 wins')
            Board()
            break
        elif sec[2] == 'X' and sec[4] == 'X' and sec[6] == 'X':
            print ('Player 1 wins')
            Board()
            break
    
        print('\n')
        
        
    else:
        Board()
        print('Player 2 pick a box')
        y = int(input("enter a number: "))
        sec[y] = 'O'

        # Player 2 victory conditions    
        if sec[0] == 'O' and sec[1] == 'O' and sec[2] == 'O':
            print ('\n\nPlayer 2 wins\n')
            Board()
            break
        elif sec[3] == 'O' and sec[4] == 'O' and sec[5] == 'O':
            print ('\n\nPlayer 2 wins\n')
            Board()
            break
        elif sec[6] == 'O' and sec[7] == 'O' and sec[8] == 'O':
            print ('\n\nPlayer 2 wins\n')
            Board()
            break
        elif sec[0] == 'O' and sec[3] == 'O' and sec[6] == 'O':
            print ('\n\nPlayer 2 wins\n')
            Board()
            break
        elif sec[1] == 'O' and sec[4] == 'O' and sec[7] == 'O':
            print ('\n\nPlayer 2 wins\n')
            Board()
            break
        elif sec[2] == 'O' and sec[5] == 'O' and sec[8] == 'O':
            print ('\n\nPlayer 2 wins\n')
            Board()
            break
        elif sec[0] == 'O' and sec[4] == 'O' and sec[8] == 'O':
            print ('\n\nPlayer 2 wins\n')
            Board()
            break
        elif sec[2] == 'O' and sec[4] == 'O' and sec[6] == 'O':
            print ('\n\nPlayer 2 wins\n')
            Board()
            break
    
    print('\n')
    x = x + 1















