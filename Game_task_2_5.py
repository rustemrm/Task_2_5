import random

player1 = 'Human'
player2 = 'Computer'
rowCells = 6
colCells = 6
fieldEmpty = " О"
fieldShip = "■"
fieldMissed = "T"
fieldShot = "X"
typeShips = [3, 2, 2, 1, 1, 1, 1]
listship=[]
Game = True
gamestep=0

class BattleField:
    def __init__(self, team):
        self.team = team
        if team == player1:
            self.hide = True
        else:
            self.hide = False
        self.field = [[fieldEmpty for i in range(rowCells)] for j in range(colCells)]

def getpoints():
    rowpoint = random.randint(0, 5)
    colpoint = random.randint(0, 5)
    return rowpoint, colpoint

def getdirection(size, rowpoint,colpoint):
    direction = random.choice(dirlist(size, rowpoint, colpoint))
    return direction

def dirlist(size,rowpoint,colpoint):
    dirlist=[1,2,3,4]
    if rowpoint < size:
        dirlist= [2,3,4]
        if colpoint < size:
          dirlist = [2,3]
        elif colpoint > 5-size:
          dirlist = [3,4]
    if rowpoint > 5-size:
        dirlist= [1,2,4]
        if colpoint < size:
          dirlist = [1,4]
        elif colpoint > 5-size:
          dirlist = [2,1]
    if colpoint < size:
        dirlist= [1,2,3]
        if rowpoint < size:
          dirlist = [2,3]
        elif rowpoint > 5-size:
          dirlist = [1,2]
    if colpoint > 5-size:
        dirlist= [1,3,4]
        if rowpoint < size:
          dirlist = [3,4]
        elif rowpoint > 5-size:
          dirlist = [4,1]
    return dirlist

def dirpoint(rowpoint,colpoint, direction):
    if direction == 1:
        rowpoint = rowpoint - 1
    elif direction == 2:
        colpoint = colpoint + 1
    elif direction == 3:
        rowpoint = rowpoint + 1
    elif direction == 4:
        colpoint = colpoint - 1
    else:
        rowpoint=-1
        colpoint=-1
    return rowpoint,colpoint

def nearPoints(team, size, rowpoint, colpoint):
    fieldpoint = battlefield1.field if team == player1 else battlefield2.field
    for k in range(int(size)):
        maxr = rowpoint+1 if rowpoint<5 else rowpoint
        minr = rowpoint-1 if rowpoint>0 else rowpoint
        rowpoints = [i for i in range(minr, maxr+1)]
        maxc = colpoint+1 if colpoint<5 else colpoint
        minc = colpoint-1 if colpoint>0 else colpoint
        colpoints = [i for i in range(minc, maxc+1)]
        i = 0
        while i < len(rowpoints):
            j = 0
            while j < len(colpoints):
                if team == player1:
                    if battlefield1.field[rowpoints[i]][colpoints[j]] == fieldShip:
                        return False
                else:
                    if battlefield2.field[rowpoints[i]][colpoints[j]] == fieldShip:
                        return False
                j +=1
            i +=1
    return True

def setShipsComp():
    team=player1
    i = 0
    count = 0
    while i < len(typeShips):
        count=count+1
        size = typeShips[i]
        number = 1
        points = []
        for j in range(size):
            rowpoint, colpoint = getpoints()
            if size == 3:
                rowpoint = 0
            direction = getdirection(size, rowpoint, colpoint)
            number = nearPoints(team,size, rowpoint, colpoint)
            number1 = True
            number2 = True
            if size == 2 or size == 3:
                rowpoint1, colpoint1 = dirpoint(rowpoint, colpoint, direction)
                number1 = nearPoints(team, size, rowpoint1, colpoint1)
            else:
                rowpoint1, colpoint1 = rowpoint, colpoint
                number1 = True
            if size == 3:
                rowpoint2, colpoint2 = dirpoint(rowpoint1, colpoint1, direction)
                number2 = nearPoints(team, size, rowpoint2, colpoint2)
            else:
                rowpoint2, colpoint2  = rowpoint,colpoint
                number2 = True
        if number and number1 and number2:
            points.append(str(rowpoint) + str(colpoint))
            battlefield1.field[rowpoint][colpoint] = fieldShip
            if size == 2 or size == 3:
                points.append(str(rowpoint1) + str(colpoint1))
                battlefield1.field[rowpoint1][colpoint1] = fieldShip
            if size == 3:
                points.append(str(rowpoint2) + str(colpoint2))
                battlefield1.field[rowpoint2][colpoint2] = fieldShip
            i = i + 1
        else:
            points = []
            if count > 2000:
                return " Ошибка ввода кораблей, повторите ввод! "
    return ' Ввод кораблей комппьтера OK!'

def setShipsHuman():
    team = player2
    i = 0
    while i < len(typeShips):
        size = typeShips[i]
        points = []
        rowpoint = checkInput1("Выберите строку корабля ",1,6)
        colpoint = checkInput1("Выберите столбец корабля ",1,6)
        rowpoint=rowpoint-1
        colpoint=colpoint-1
        print(" ------------------------------------------")
        if size > 1:
            print(" 1 - вверх, 2 - вправо, 3 - вниз, 4 - влево")
            print(" ------------------------------------------")
            listdir = dirlist(size, rowpoint, colpoint)
            direction = checkInput2("Выберите направление ", listdir)
        else:
            direction = 1
        number = nearPoints(team, size, rowpoint, colpoint)
        number1 = True
        number2 = True
        rowpoint1, colpoint1 = dirpoint(rowpoint, colpoint, direction)
        rowpoint2, colpoint2 = dirpoint(rowpoint1, colpoint1, direction)
        if size == 2 or size == 3:
            number1 = nearPoints(team, size, rowpoint1, colpoint1)
        if size == 3:
            number2 = nearPoints(team, size, rowpoint2, colpoint2)
        if number and number1 and number2:
            points.append(str(rowpoint) + str(colpoint))
            battlefield2.field[rowpoint][colpoint] = fieldShip
            if size == 2 or size == 3:
                points.append(str(rowpoint1) + str(colpoint1))
                battlefield2.field[rowpoint1][colpoint1] = fieldShip
            if size == 3:
                points.append(str(rowpoint2) + str(colpoint2))
                battlefield2.field[rowpoint2][colpoint2] = fieldShip
            drawFilds(team, rowpoint, colpoint)
            i=i+1
        else:
            print(" Ошибка ввода корабля, повторите ввод!")
    return ' Ввод кораблей Игрока OK!'

def drawFilds(team, rowpoint, colpoint):
    if team == player1:
        fieldpoint = battlefield1.field
    else:
        fieldpoint = battlefield2.field
    count1 = 0
    count2 = 0
    i = 0
    print('\n ')
    print('  |1 |2 |3 |4 |5 |6 |      |1 |2 |3 |4 |5 |6 |\n')
    while i <= 5:
        j = 0
        n = str(i + 1) + ' |'
        n1 = str(i + 1) + ' |'
        while j <= 5:
            if battlefield1.field[i][j] == fieldShip:
                count1 += 1
            if battlefield2.field[i][j] == fieldShip:
                count2 += 1
            if gamestep == 1:
                if rowpoint-1 == i and colpoint-1 == j:
                    if fieldpoint[i][j] == fieldShip:
                        fieldpoint[i][j] = fieldShot
                    else:
                        fieldpoint[i][j] = fieldMissed
            if battlefield1.hide and battlefield1.field[i][j] == fieldShip:
                n = n + fieldEmpty + '|'
            else:
                n = n + battlefield1.field[i][j] + '|'
            n1 = n1 + battlefield2.field[i][j] + '|'
            j = j + 1
        i = i + 1
        print(n + '    ' + n1)
        print('')
    if gamestep == 1 and count2 == 0:
        input(" Игра закончена - победитель Компьютер")
    if gamestep == 1 and count1 == 0:
        input(" Игра закончена - победитель Игрок")
    return count1, count2

def playGame():
    while Game:
        move = 0
        Message1 =" Игрок сделайте ход !"
        while move == 0:
            team = player1
            print(f"  {Message1}                            |")
            print("-----------------------------------------")
            rowpoint = checkInput1("Выберите строку корабля ",1,6)
            colpoint = checkInput1("Выберите столбец корабля ",1,6)
            print("-----------------------------------------")
            count1,count2 = drawFilds(team, rowpoint,colpoint)
            if gamestep == 1 and count1 == 0:
                input(" Игра закончена - победитель Игрок")
                return
            if battlefield1.field[rowpoint-1][colpoint-1] == fieldShip:
                move = 0
            else:
                move = 1
        while move == 1:
            team = player2
            rowpoint, colpoint = getpoints()
            if battlefield2.field[rowpoint][colpoint] == fieldMissed or battlefield2.field[rowpoint][colpoint] == fieldShot:
                move = 1
            else:
                count1,count2 = drawFilds(team, rowpoint+1, colpoint+1)
                if gamestep == 1 and count2 == 0:
                    input(" Игра закончена - победитель Компьютер")
                    return
                if battlefield2.field[rowpoint][colpoint] == fieldShip:
                    move =1
                else:
                    move = 0
    return

def checkInput1(text, startValue, endValue):
    while True:
        try:
            inputValue = int(input(text))
            if inputValue >=int(startValue) and inputValue<=int(endValue):
                return inputValue
        except ValueError:
            True
        print("Ошибка ввода!")

def checkInput2(text, list):
    while True:
        try:
            inputValue = int(input(text))
            if inputValue in list:
                return inputValue
        except ValueError:
            True
        print("Ошибка ввода!")

battlefield1 = BattleField(player1)
battlefield2 = BattleField(player2)
Message= ''
while Game:

    print("     Игра Морской бой   ")
    print("-----------------------------------------")

    print(f"  {Message}                            ")
    print("-----------------------------------------")
    print("  Ввод кораблей компьютера------------- 1 ")
    print("  Показать/Скрыть корабли компьютера -- 2 ")
    print("  Ввод кораблей игрока    ------------- 3 ")
    print("  Начало игры ------------------------- 4 ")
    print("  Выход из игры ----------------------- 5 ")
    print("-----------------------------------------")
    MenuChoice=checkInput1("  Выберите пункт меню:         ",1,5)
    if MenuChoice == 1:
        gamestep = 0
        battlefield1 = BattleField(player1)
        Message = setShipsComp()
        battlefield2 = BattleField(player2)
        count1, count2 = drawFilds('',7,7)
    elif MenuChoice == 2:
        gamestep = 0
        print("  Показать корабли------------------ 1 ")
        print("  Скрыть корабли-------------------- 2 ")
        print("-----------------------------------------")
        MenuChoice1 = checkInput1("  Выберите пункт меню:         ", 1, 2)
        if MenuChoice1 == 1:
            battlefield1.hide = False
        else:
            battlefield1.hide = True
        count1, count2 = drawFilds('',7,7)
    elif MenuChoice == 3:
        gamestep = 0
        Message = setShipsHuman()
        count1, count2v= drawFilds('',7,7)
    elif MenuChoice == 4 :
        count1, count2 = drawFilds('',7,7)
        if count1 <11 and count2 <11:
            Message=" Выбор кораблей не завершен! "
        else:
            gamestep=1
            playGame()
    elif MenuChoice == 5:
        Game = False