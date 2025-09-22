def validator(board):
    totalcolor = {'w':0, 'b':0}
    pawn_count = {'w':0, 'b':0}
    
    for square, piece in board.items():
        # Check piece color
        color = piece[0]
        ptype = piece[1:]  # e.g., 'K', 'Q', 'P'
        
        if color not in ('w','b') or ptype not in ('P','R','N','B','Q','K'):
            print("invalid piece")
            return False
        
        # Count total pieces
        totalcolor[color] += 1
        
        # Count pawns
        if ptype == 'P':
            pawn_count[color] += 1
            if pawn_count[color] > 8:
                print("too many pawns")
                return False
        
        # Check square validity
        if len(square) != 2 or square[0] not in '12345678' or square[1] not in 'abcdefgh':
            print("invalid square")
            return False
        
    # Check total pieces <=16
    if totalcolor['w'] > 16 or totalcolor['b'] > 16:
        print("too many pieces")
        return False
    
    # Check exactly one king each
    kings = [p for p in board.values() if p[1:] == 'K']
    if kings.count('wK') != 1 or kings.count('bK') != 1:
        print("wrong number of kings")
        return False
    
    print("valid board")
    return True
def menu():
    print("-----------------------------")
    print("welcome to board validator")
    print("input board")
    board = input()
    validator(board)