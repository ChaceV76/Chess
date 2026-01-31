# We will create classes for each specific piece

class Pawn:
    pass

class Bishop:
    pass

class Knight:
    pass

class Rook:
    pass

class Queen(Bishop, Rook):
    pass

class King(Queen):
    pass


# Create class for teams inherting all the pieces
class White(Pawn, Bishop, Knight, Rook, Queen, King):
    pass

class Black(Pawn, Bishop, Knight, Rook, Queen, King):
    pass