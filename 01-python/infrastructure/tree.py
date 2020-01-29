def draw_tree(height=5):
    """main function to draw a tree
       the variable height is the height of the leaves"""
    draw_leaves(height)
    draw_trunk(height)

    return


def draw_leaves(height):
    """drawing the leaves part of the tree
        input: a height int variable"""
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
    """ drawing the trunk part of the tree
        input : a height int variable"""
    for i in range(height-3):
        s = " " *(height-1) + "|" + " " + "|" 
        print(s)
    
    return          
