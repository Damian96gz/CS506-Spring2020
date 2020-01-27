def draw_tree():
    #print("tree not found")
    draw_leaves()
    draw_trunk()

    return


def draw_leaves():
    for i in range(5):
        leaves = ""
        for j in range(10):
             if j < 5-i:
                leaves += " "
             elif j > 5+i:
                leaves += " "
             else:
                leaves += "*"
        print(leaves)
    return

def draw_trunk():
    for i in range(3):
        s = " " *4 + "|" + " " + "|" + " "*3
        print(s)
    return          
