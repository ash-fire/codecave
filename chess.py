from turtle import *
sc = Screen()

fillcolor()
speed(1000)
setup( width = 800, height = 800, startx = None, starty = None) 
def square():
    fd(100)
    rt(90)
    fd(100)
    rt(90)
    fd(100)
    rt(90)
    fd(100)
    rt(90)
    fd(100)
def up():
    pu()
    setx(-window_width() / 2)
    sety(ycor() + 100)
    pd()    

def move(clicked, x, y):
    
    def ukey():
        clicked.fd(100)
    def dkey():
        clicked.bk(100)
    def lkey():
        clicked.lt(90)
    def rkey():
        clicked.rt(90)
    sc.onkey(ukey, "Up")
    sc.onkey(dkey, "Down")
    sc.onkey(lkey, "Left")
    sc.onkey(rkey, "Right")
    sc.listen()

pu()
setx(-window_width() / 2)
sety(-window_height() / 2 + 100)
pd()
for y in range(1,9):
    for x in range(1,9):
        if (x + y) % 2 == 0:
            begin_fill()
            square()
            end_fill()
        else:
            square()
    up()


    

# PAWNS
whitepawn = "chess_pieces/white_pawn.gif"
sc.addshape(whitepawn)
wp1 = Turtle()
wp1.pu()
wp1.shape(whitepawn)
wp1.setx(-350)
wp1.sety(250)

whitepawn2 = "chess_pieces/white_pawn2.gif"
sc.addshape(whitepawn2)
wp2 = Turtle()
wp2.pu()
wp2.shape(whitepawn2)
wp2.setx(-250)
wp2.sety(250)

whitepawn3 = "chess_pieces/white_pawn3.gif"
sc.addshape(whitepawn3)
wp3 = Turtle()
wp3.pu()
wp3.shape(whitepawn3)
wp3.setx(-150)
wp3.sety(250)

whitepawn4 = "chess_pieces/white_pawn4.gif"
sc.addshape(whitepawn4)
wp4 = Turtle()
wp4.pu()
wp4.shape(whitepawn4)
wp4.setx(-50)
wp4.sety(250)

whitepawn5 = "chess_pieces/white_pawn5.gif"
sc.addshape(whitepawn5)
wp5 = Turtle()
wp5.pu()
wp5.shape(whitepawn5)
wp5.setx(50)
wp5.sety(250)

whitepawn6 = "chess_pieces/white_pawn6.gif"
sc.addshape(whitepawn6)
wp6 = Turtle()
wp6.pu()
wp6.shape(whitepawn6)
wp6.setx(150)
wp6.sety(250)

whitepawn7 = "chess_pieces/white_pawn7.gif"
sc.addshape(whitepawn7)
wp7 = Turtle()
wp7.pu()
wp7.shape(whitepawn7)
wp7.setx(250)
wp7.sety(250)

whitepawn8 = "chess_pieces/white_pawn8.gif"
sc.addshape(whitepawn8)
wp8 = Turtle()
wp8.pu()
wp8.shape(whitepawn8)
wp8.setx(350)
wp8.sety(250)

blackpawn = "chess_pieces/black_pawn.gif"
sc.addshape(blackpawn)
bp1 = Turtle()
bp1.pu()
bp1.shape(blackpawn)
bp1.setx(-350)
bp1.sety(-250)

blackpawn2 = "chess_pieces/black_pawn2.gif"
sc.addshape(blackpawn2)
bp2 = Turtle()
bp2.pu()
bp2.shape(blackpawn2)
bp2.setx(-250)
bp2.sety(-250)

blackpawn3 = "chess_pieces/black_pawn3.gif"
sc.addshape(blackpawn3)
bp3 = Turtle()
bp3.pu()
bp3.shape(blackpawn3)
bp3.setx(-150)
bp3.sety(-250)

blackpawn4 = "chess_pieces/black_pawn4.gif"
sc.addshape(blackpawn4)
bp4 = Turtle()
bp4.pu()
bp4.shape(blackpawn4)
bp4.setx(-50)
bp4.sety(-250)

blackpawn5 = "chess_pieces/black_pawn5.gif"
sc.addshape(blackpawn5)
bp5 = Turtle()
bp5.pu()
bp5.shape(blackpawn5)
bp5.setx(50)
bp5.sety(-250)

blackpawn6 = "chess_pieces/black_pawn6.gif"
sc.addshape(blackpawn6)
bp6 = Turtle()
bp6.pu()
bp6.shape(blackpawn6)
bp6.setx(150)
bp6.sety(-250)

blackpawn7 = "chess_pieces/black_pawn7.gif"
sc.addshape(blackpawn7)
bp7 = Turtle()
bp7.pu()
bp7.shape(blackpawn7)
bp7.setx(250)
bp7.sety(-250)

blackpawn8 = "chess_pieces/black_pawn8.gif"
sc.addshape(blackpawn8)
bp8 = Turtle()
bp8.pu()
bp8.shape(blackpawn8)
bp8.setx(350)
bp8.sety(-250)

# BISHOPS, ROOKS, KNIGHTS

whitebishop = "chess_pieces/white_bishop.gif"
sc.addshape(whitebishop)
wb1 = Turtle()
wb1.pu()
wb1.shape(whitebishop)
wb1.setx(-150)
wb1.sety(350)

whitebishop2 = "chess_pieces/white_bishop2.gif"
sc.addshape(whitebishop2)
wb2 = Turtle()
wb2.pu()
wb2.shape(whitebishop2)
wb2.setx(150)
wb2.sety(350)

blackbishop = "chess_pieces/black_bishop.gif"
sc.addshape(blackbishop)
bb1 = Turtle()
bb1.pu()
bb1.shape(blackbishop)
bb1.setx(-150)
bb1.sety(-350)

blackbishop2 = "chess_pieces/black_bishop2.gif"
sc.addshape(blackbishop2)
bb2 = Turtle()
bb2.pu()
bb2.shape(blackbishop2)
bb2.setx(150)
bb2.sety(-350)

whiterook = "chess_pieces/white_rook.gif"
sc.addshape(whiterook)
wr1 = Turtle()
wr1.pu()
wr1.shape(whiterook)
wr1.setx(-350)
wr1.sety(350)

whiterook2 = "chess_pieces/white_rook2.gif"
sc.addshape(whiterook2)
wr2 = Turtle()
wr2.pu()
wr2.shape(whiterook2)
wr2.setx(350)
wr2.sety(350)

blackrook = "chess_pieces/black_rook.gif"
sc.addshape(blackrook)
br1 = Turtle()
br1.pu()
br1.shape(blackrook)
br1.setx(-350)
br1.sety(-350)

blackrook2 = "chess_pieces/black_rook2.gif"
sc.addshape(blackrook2)
br2 = Turtle()
br2.pu()
br2.shape(blackrook2)
br2.setx(350)
br2.sety(-350)

whiteknight = "chess_pieces/white_knight.gif"
sc.addshape(whiteknight)
wk1 = Turtle()
wk1.pu()
wk1.shape(whiteknight)
wk1.setx(-250)
wk1.sety(350)

whiteknight2 = "chess_pieces/white_knight2.gif"
sc.addshape(whiteknight2)
wk2 = Turtle()
wk2.pu()
wk2.shape(whiteknight2)
wk2.setx(250)
wk2.sety(350)

blackknight = "chess_pieces/black_knight.gif"
sc.addshape(blackknight)
bk1 = Turtle()
bk1.pu()
bk1.shape(blackknight)
bk1.setx(-250)
bk1.sety(-350)

blackknight2 = "chess_pieces/black_knight2.gif"
sc.addshape(blackknight2)
bk2 = Turtle()
bk2.pu()
bk2.shape(blackknight2)
bk2.setx(250)
bk2.sety(-350)

# KINGS, QUEENS
whiteking = "chess_pieces/white_king.gif"
sc.addshape(whiteking)
wk = Turtle()
wk.pu()
wk.shape(whiteking)
wk.setx(-50)
wk.sety(350)

whitequeen = "chess_pieces/white_queen.gif"
sc.addshape(whitequeen)
wq = Turtle()
wq.pu()
wq.shape(whitequeen)
wq.setx(50)
wq.sety(350)

blackking = "chess_pieces/black_king.gif"
sc.addshape(blackking)
bk = Turtle()
bk.pu()
bk.shape(blackking)
bk.setx(-50)
bk.sety(-350)

blackqueen = "chess_pieces/black_queen.gif"
sc.addshape(blackqueen)
bq = Turtle()
bq.pu()
bq.shape(blackqueen)
bq.setx(50)
bq.sety(-350)
onclick(move)





    

