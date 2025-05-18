white = {
    'pawns': ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
    'knights': ['b1', 'g1'],
    'bishops': ['c1', 'f1'],
    'rooks': ['a1', 'h1'],
    'queen': ['d1'],
    'king': ['e1']
}

black = {
    'pawns': ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
    'knights': ['b8', 'g8'],
    'bishops': ['c8', 'f8'],
    'rooks': ['a8', 'h8'],
    'queen': ['d8'],
    'king': ['e8']
}

Constants = {
    'Number of moves': 0
}

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
pieces = ('pawns', 'knights', 'bishops', 'rooks', 'queen', 'king')
players = ('white', 'black')
Board = {'Occupied squares': [], 'Empty squares': []}


def Populate_board():
    for y in range(len(pieces)):
        a = pieces[y]
        piece = white[a]
        for z in range(len(piece)):
            (Board['Occupied squares']).append(piece[z])
    
    for y in range(len(pieces)):
        a = pieces[y]
        piece = black[a]
        for z in range(len(piece)):
            (Board['Occupied squares']).append(piece[z])

# Check the unoccupied squares at the start of the game and append them to dictionary as a list
def Unoccpied_squares():
    for x in range(len(letters)):
        for y in range(1,9):
            if (str(letters[x])+str(y)) in Board['Occupied squares']:
                pass
            else:
                Board['Empty squares'].append((str(letters[x])+str(y)))

def king():
    location = white[pieces[5]]
    location = location[0]
    print(location)
    possible = []
    horizontal = location[0]
    vertical = int(location[1])
    for x in range(len(letters)):
        if horizontal == letters[x]:
            horizontal = int(x)

    print(horizontal)
    print(vertical)

    possible.append(str(letters[horizontal-1])+str(vertical-1))
    possible.append(str(letters[horizontal-1])+str(vertical))
    possible.append(str(letters[horizontal-1])+str(vertical+1))
    possible.append(str(letters[horizontal])+str(vertical-1))
    possible.append(str(letters[horizontal])+str(vertical))
    possible.append(str(letters[horizontal])+str(vertical+1))
    possible.append(str(letters[horizontal+1])+str(vertical-1))
    possible.append(str(letters[horizontal+1])+str(vertical))
    possible.append(str(letters[horizontal+1])+str(vertical+1))
    
    print(possible)
king()