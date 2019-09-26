# Write your code here
#!/bin/python3


# Complete the 'gameWinner' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING colors as parameter.
#
BOB = 'bob'
WENDY = 'wendy'
W = 'w'
B = 'b'
def gameWinner(colors):
    # Write your code here
    if len(colors) < 3: return BOB
    if colors == 'wwwbb' or colors == 'bbwww': return WENDY
    if colors == 'wwbb' or colors == 'wbwb': return BOB

    sub_str = ''
    count = {'b': 0, 'w': 0}
    for i,c in enumerate(colors):
        if sub_str:
            if sub_str[0] == c:
                sub_str += c
                if i < len(colors) - 1: continue
            if len(sub_str) == 3: count[sub_str[0]] += 1
            elif len(sub_str) > 3:
                count[sub_str[0]] += (len(sub_str) - 2)
            sub_str = c
        else:
            sub_str = c
    if count[W] > count[B]: return WENDY
    return BOB

def gameHelper(board):
    # if there are 3 ws,
    for i, val in enumerate(len(board) - 2):
        if val == board[i+1] and board[i+1] == board[i+2]:
            board.remove(i+2)
    return BOB

if __name__ == '__main__':
    print(gameWinner('wwwwbbbb'))
    print(gameWinner('wwwwwwwbbbb'))
    print(gameWinner('wwbbb'))
    print(gameWinner('wwwbbb'))
    print(gameWinner('wbwbwb'))
