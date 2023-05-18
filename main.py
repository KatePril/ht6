def mouse(symbol):
    symbol *= 2
    
    print(symbol)
    print(symbol + "  " * 2 + symbol * 2)
    print("  " + symbol * 2 + "  " * 2 + symbol)
    print("  " * 5 + symbol)
    print("  " * 3 + symbol * 5)
    for i in range(2):
        print("  " * 2 + symbol + "  " * 2 + symbol + "  " * 2 + symbol)
    print("  " * 2 + symbol * 7)
    for i in range(4):
        print("  " * 2 + symbol + "  " * 5 + symbol)
    print("  " * 3 + symbol + "  " * 3 + symbol)
    print("  " * 4 + symbol * 3)

def draw_mouse():
    print("MOUSE")
    symbol = input("Enter the symbol: ")
    mouse(symbol[0])


def planet(symbol):
    symbol *= 2
    
    print("  " * 5 + symbol * 4)
    print("  " * 4 + symbol + "  " * 4 + symbol)
    print("  " + symbol * 3 + "  " * 6 + symbol * 3)
    print(symbol + "  " * 2 + symbol + "  " * 6 + symbol + "  " * 2 + symbol)
    print("  " + symbol * 12)
    print("  " * 4 + symbol + "  " * 4 + symbol)
    print("  " * 5 + symbol * 4)
    
def draw_planet():
    print("PLANET")
    symbol = input("Enter the symbol: ")
    planet(symbol[0])


def owl(main_symbol, additional_symbol, another_additional_symbol):
    main_symbol *= 2
    additional_symbol *= 2
    another_additional_symbol *= 2
    
    for el in [[4, 5], [3, 7], [2, 9]]:
        print("  " * el[0] + main_symbol * el[1])
    print("  " * 2 + main_symbol * 2 + "  " * 2 + main_symbol + "  " * 2 + main_symbol * 2)
    print("  " * 2 + main_symbol * 2 + "  " + another_additional_symbol + "  " + another_additional_symbol + "  " + main_symbol * 2)
    print("  " + main_symbol * 3 + "  " * 2 + additional_symbol + "  " * 2 + main_symbol * 3)
    print(main_symbol * 13)
    for i in range(3):
        print(main_symbol * 4 + "  " * 5 + main_symbol * 4)
    print("  " + main_symbol * 3 + "  " * 5 + main_symbol * 3)
    for el in [[2, 9], [3, 7]]:
        print("  " * el[0] + main_symbol * el[1])
    print("  " * 4 + additional_symbol + "  " * 3 + additional_symbol)
    print("  " * 3 + additional_symbol * 3 + "  " + additional_symbol * 3)

def draw_owl():
    print("OWL")
    main_symbol = input("Enter the main symbol: ")
    additional_symbol = input("Enter the additional symbol: ")
    another_additional_symbol = input("Enter another additional symbol: ")
    owl(main_symbol[0], additional_symbol[0], another_additional_symbol[0])


def penguin(main_symbol, additional_symbol):
    main_symbol *= 2
    additional_symbol *= 2
    
    for el in [[6, 7], [5, 9], [4, 11]]:
        print("  " * el[0] + main_symbol * el[1])
    for el in [[3, 2, 3, 3, 3, 2], [2, 2, 5, 1, 5, 2], [2, 2, 5, 1, 5, 2]]:
        print("  " * el[0] + main_symbol * el[1] + "  " * el[2] + main_symbol * el[3] + "  " * el[4] + main_symbol * el[5])
    for el in [[4, 1, 3, 1, 4], [3, 2, 3, 2, 3], [3, 2, 3, 2, 3]]:
        print("  " + main_symbol * 2 + "  " * el[0] + main_symbol * el[1] + "  " * el[2] + main_symbol * el[3] + "  " * el[4] + main_symbol * 2)
    print("  " + main_symbol * 2 + "  " * 13 + main_symbol * 2 )
    for el in [[1, 2, 5, 3, 5, 2], [1, 3, 3, 5, 3, 3], [2, 3, 2, 5, 2, 3], [3, 5, 0, 3, 0, 5]]:
        print("  " * el[0] + main_symbol * el[1] + "  " * el[2] + additional_symbol * el[3] + "  " * el[4] + main_symbol * el[5])
    print("  " * 3 + main_symbol * 13)
    for el in [[2, 5, 5, 5], [2, 3, 9, 3], [1, 3, 11, 3]]:
        print("  " * el[0] + main_symbol * el[1] + "  " * el[2] + main_symbol * el[3])
    print(main_symbol * 4 + additional_symbol + "  " + additional_symbol + "  " * 4 + "  " + additional_symbol + "  " + additional_symbol + main_symbol * 4)
    for el in [[3, 5, 3, 5, 3], [2, 7, 1, 7, 2], [2, 7, 1, 7, 2]]:
        print(main_symbol * el[0] + additional_symbol * el[1] + "  " * el[2] + additional_symbol * el[3] + main_symbol * el[4])
    print("  " + main_symbol * 1 + additional_symbol * 7 + "  " * 1 + additional_symbol * 7 + main_symbol * 1)
    print("  " * 2 + main_symbol * 2 + additional_symbol * 3 + main_symbol * 5 + additional_symbol * 3 + main_symbol * 2)
    print("  " * 3 + main_symbol * 2 + additional_symbol + main_symbol + "  " * 5 + main_symbol + additional_symbol + main_symbol * 2)

def draw_penguin():
    print("PENGUIN")
    main_symbol = input("Enter the main symbol: ")
    additional_symbol = input("Enter the additional symbol: ")
    penguin(main_symbol[0], additional_symbol[0])


draw_mouse()
draw_planet()
draw_owl()
draw_penguin()