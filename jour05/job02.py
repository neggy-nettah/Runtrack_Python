

def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1: # première et dernière ligne 
            print("|" + "-" * (width - 2) + "|") 
        else:
            print("|" + " " * (width - 2) + "|")

    print()
draw_rectangle(10, 3)

def draw_rectangle(whidth, height):
    c= "|" + "-" * (whidth -2) + "|\n";
    print(c + (c.replace ( * "- ")) * (height -2) + c)

draw_rectangle(10,3)