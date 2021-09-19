from random import randint

"""
1- Start with a score of 0,
2- If all four corners are even numbers, add 20 pts to the score,
3- If all four corners are odd numbers, add 20 pts to the score,
4- If all four dice on a diagonal are even numbers, add 20 pts to the score,
5- If all four dice on a diagonal are odd numbers, add 20 pts to the score,
6-If all four dice on on any row are even numbers, add 20 pts to the score,
7- If all four dice on on any row are odd numbers, add 20 pts to the score,
8- If all four dice on on any column are even numbers, add 20 pts to the score,
9- If all four dice on on any column are odd numbers, add 20 pts to the score,
10- Add to the score the total value (sum) of all 16 dice

"""
"""
1- 0 puanla başlayın,
2- Dört köşenin tümü çift sayı ise, skora 20 puan ekleyin
3- Dört köşenin tümü tek sayıysa, skora 20 puan ekleyin
4- Köşegendeki dört zarın tümü çift sayıysa, skora 20 puan ekleyin
5- Köşegendeki dört zarın tümü tek sayıysa, skora 20 puan ekleyin
6- Herhangi bir satırdaki dört zarın tümü çift sayı ise, skora 20 puan ekleyin
7- Herhangi bir satırdaki dört zarın tümü tek sayıysa, skora 20 puan ekleyin
8- Herhangi bir sütundaki dört zarın tümü çift sayıysa, puana 20 puan ekleyin
9- Herhangi bir sütundaki dört zarın tümü tek sayıysa, skora 20 puan ekleyin
10- 16 zarın toplam değerini (toplamını) puana ekleyin
"""

grid = []

# A new 4-by-4 grid of 16 dice
# 16 zardan oluşan yeni bir 4'e 4 grid


def yenilemeGrid():
    global grid
    grid = []
    for satir in range(4):
        grid.append([])
        for col in range(4):
            zar = randint(1, 6)
            grid[satir].append(zar)

# view the dice grid
# Zar gridini görüntülemek


def gosterGrid():
    global grid
    for satir in range(4):
        st = "| "
        for sutun in range(4):
            st = st + str(grid[satir][sutun]) + " | "
        print(st)

# Check if a number is even
# Bir sayının çift sayı olup olmadığını kontrol etme


def isEven(sayi):
    if sayi % 2 == 0:
        return True
    else:
        return False

# Check if a number is odd
# Bir sayının tek sayı olup olmadığını kontrol etme


def isOdd(sayi):
    if sayi % 2 == 1:
        return True
    else:
        return False


#
yenilemeGrid()
gosterGrid()
score = 0

# Dört köşedeki tüm sayıların çift sayı olup olmadığını kontrol etme
# Check if the four corners are even numbers

if isEven(grid[0][0]) and isEven(grid[0][3]) and isEven(grid[3][0]) and isEven(grid[3][3]):
    print("Four even corners! +20pts")
    score = score + 20

# Dört köşedeki tüm sayıların tek sayı olup olmadığını kontrol etme
# Check if the four corners are odd numbers

if isOdd(grid[0][0]) and isOdd(grid[0][3]) and isOdd(grid[3][0]) and isOdd(grid[3][3]):
    print("Four odd corners! +20pts")
    score = score + 20

# Köşegendeki dört zarın tümü çift sayı olup olmadığını kontrol etme
# Check if the four on a diagonal are even numbers

if isEven(grid[0][0]) and isEven(grid[1][1]) and isEven(grid[2][2]) and isEven(grid[3][3]):
    print("Four even diagonels! +20pts")
    score = score + 20
if isEven(grid[0][3]) and isEven(grid[1][2]) and isEven(grid[2][1]) and isEven(grid[3][0]):
    print("Four even diagonels! +20pts")
    score = score + 20

# Köşegendeki dört zarın tümü tek sayı olup olmadığını kontrol etme
# Check if the four on a diagonal are odd numbers

if isOdd(grid[0][0]) and isOdd(grid[1][1]) and isOdd(grid[2][2]) and isOdd(grid[3][3]):
    print("Four odd diagonal! +20pts")
    score = score + 20
if isOdd(grid[0][3]) and isOdd(grid[1][2]) and isOdd(grid[2][1]) and isOdd(grid[3][0]):
    print("Four odd diagonel! +20pts")
    score = score + 20

# Herhangi bir satırdaki dört zarın tümü çift sayı olup olmadığını kontrol etme
# Check if all four dice on any row are even numbers

if isEven(grid[0][0]) and isEven(grid[0][1]) and isEven(grid[0][2]) and isEven(grid[0][3]):
    print("Four even rows! +20pts")
    score = score + 20
if isEven(grid[1][0]) and isEven(grid[1][1]) and isEven(grid[1][2]) and isEven(grid[1][3]):
    print("Four even rows! +20pts")
    score = score + 20
if isEven(grid[2][0]) and isEven(grid[2][1]) and isEven(grid[2][2]) and isEven(grid[2][3]):
    print("Four even rows! +20pts")
    score = score + 20
if isEven(grid[3][3]) and isEven(grid[3][1]) and isEven(grid[3][2]) and isEven(grid[3][3]):
    print("Four even rows! +20pts")
    score = score + 20

# Herhangi bir satırdaki dört zarın tümü tek sayı olup olmadığını kontrol etme
# Check if all four dice on any row are odd numbers


if isOdd(grid[0][0]) and isOdd(grid[0][1]) and isOdd(grid[0][2]) and isOdd(grid[0][3]):
    print("Four even rows! +20pts")
    score = score + 20
if isOdd(grid[1][0]) and isOdd(grid[1][1]) and isOdd(grid[1][2]) and isOdd(grid[1][3]):
    print("Four even rows! +20pts")
    score = score + 20
if isOdd(grid[2][0]) and isOdd(grid[2][1]) and isOdd(grid[2][2]) and isOdd(grid[2][3]):
    print("Four even rows! +20pts")
    score = score + 20
if isOdd(grid[3][3]) and isOdd(grid[3][1]) and isOdd(grid[3][2]) and isOdd(grid[3][3]):
    print("Four even rows! +20pts")
    score = score + 20

# Herhangi bir sütundaki dört zarın tümü çift sayı olup olmadığını kontrol etme
# Check if all for dice on any column are even numbers

if isEven(grid[0][0]) and isEven(grid[1][0]) and isEven(grid[2][0]) and isEven(grid[3][0]):
    print("Four even columns! +20pts")
    score = score + 20
if isEven(grid[0][1]) and isEven(grid[1][1]) and isEven(grid[2][1]) and isEven(grid[3][1]):
    print("Four even columns! +20pts")
    score = score + 20
if isEven(grid[0][2]) and isEven(grid[1][2]) and isEven(grid[2][2]) and isEven(grid[3][2]):
    print("Four even columns! +20pts")
    score = score + 20
if isEven(grid[0][3]) and isEven(grid[1][3]) and isEven(grid[2][3]) and isEven(grid[3][3]):
    print("Four even columns! +20pts")
    score = score + 20

# Herhangi bir sütundaki dört zarın tümü tek sayı olup olmadığını kontrol etme
# Check if all for dice on any column are odd numbers

if isOdd(grid[0][0]) and isOdd(grid[1][0]) and isOdd(grid[2][0]) and isOdd(grid[3][0]):
    print("Four even columns! +20pts")
    score = score + 20
if isOdd(grid[0][1]) and isOdd(grid[1][1]) and isOdd(grid[2][1]) and isOdd(grid[3][1]):
    print("Four even columns! +20pts")
    score = score + 20
if isOdd(grid[0][2]) and isOdd(grid[1][2]) and isOdd(grid[2][2]) and isOdd(grid[3][2]):
    print("Four even columns! +20pts")
    score = score + 20
if isOdd(grid[0][3]) and isOdd(grid[1][3]) and isOdd(grid[2][3]) and isOdd(grid[3][3]):
    print("Four even columns! +20pts")
    score = score + 20

# 16 zarın toplam değerini (toplamını) puana ekleyin
# Add to the score the total value (sum) of all 16 dice.
totalScore = score + grid[0][0]+grid[0][1]+grid[0][2]+grid[0][3]+grid[1][0]+grid[1][1] + \
    grid[1][2]+grid[1][3]+grid[2][0]+grid[2][1]+grid[2][2] + \
    grid[2][3]+grid[3][0]+grid[3][1]+grid[3][2]+grid[3][3]


print("\nGrid score: " + str(score) + " pts.")
print("\nTotal score: " + str(totalScore) + " pts.")
