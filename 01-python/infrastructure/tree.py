def draw_tree(height=5):
    draw_leaves(height)
    draw_trunk(height)

    return


def draw_leaves(height):
    for i in range(height):
        leaves = ""
        for j in range(2*height):
             if j < height-i:
                leaves += " "
             elif j > height+i:
                leaves += " "
             else:
                leaves += "*"
        print(leaves)
    return

def draw_trunk(height):

    for i in range(height-3):
        s = " " *(height-1) + "|" + " " + "|" 
        print(s)
    
    return          
