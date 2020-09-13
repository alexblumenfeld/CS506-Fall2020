def draw_firestation(trucks=1):
    print("________________")
    print("|_|_||_||_||_|_|")
    print("|  |  |  |  |  |")
    print("|  F  I  R  E  |")
    print("|  D  E  P  T  |")
    print("|  __________  |")
    print("|  |        |  |" + "  ==================" * trucks)
    print("|  | []  [] |  |" + "  _|_|___|__|__|_   " * trucks)
    print("|  |        |  |" + "  |              |-|" * trucks)  
    print("|  | []  [] |  |" + "  |________________|" * trucks)
    print("|  |        |  |" + "    []         []   " * trucks)
    print("----------------" + "--------------------" * trucks)
    return
