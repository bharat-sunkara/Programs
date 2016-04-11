Board = {'top-L':' ', 'top-M':' ', 'top-R':' ',
         'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
         'low-L':' ', 'low-M':' ', 'low-R':' '}

def printboard(iboard):
    print(iboard['top-L'] + '|' + iboard['top-M'] + '|' + iboard['top-R'])
    print('-+-+-')
    print(iboard['mid-L'] + '|' + iboard['mid-M'] + '|' + iboard['mid-R'])
    print('-+-+-')
    print(iboard['low-L'] + '|' + iboard['low-M'] + '|' + iboard['low-R'])

turn = 'X'
count = 0
for i in range(9):
    count += 1
    printboard(Board)
    print('Turn for ' + turn)
    move = input()
    Board[move] = turn

    if count >= 6:
        if Board['top-L'] == Board['top-M'] == Board['top-R']:
            print('Game over! ' + turn + ' wins!')
            break
        elif:
            Board['mid-L'] == Board['mid-M'] == Board['mid-R']:
            print('Game over! ' + turn + ' wins!')
            break
        elif:
            Board['low-L'] == Board['low-M'] == Board['low-R']:
            print('Game over! ' + turn + ' wins!')
            break
        elif:
            Board['top-L'] == Board['mid-L'] == Board['low-L']:
            print('Game over! ' + turn + ' wins!')
            break
        elif:
            Board['top-R'] == Board['mid-R'] == Board['low-R']:
            print('Game over! ' + turn + ' wins!')
            break
        elif:
            Board['top-M'] == Board['mid-M'] == Board['low-M']:
            print('Game over! ' + turn + ' wins!')
            break        
        elif:
            Board['top-L'] == Board['mid-M'] == Board['low-R']:
            print('Game over! ' + turn + ' wins!')
            break
        else:
            Board['top-R'] == Board['mid-M'] == Board['low-L']:
            print('Game over! ' + turn + ' wins!')
            break        
        
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
        
printboard(Board)
        
    
