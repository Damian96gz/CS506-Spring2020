<<<<<<< HEAD
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
=======
def draw_tree(height = 5):
    """
        draw a tree:
          o
         ooo
        ooooo
          o

        :param: height: the height of tree
    """

    MIN_HEIGHT = 3

    # height check
    if (height < MIN_HEIGHT) :
        raise ValueError("Invalid height, tree height must be greater than " + str(MIN_HEIGHT) + ".")

    else :
        print("found a beautiful tree.")

        # print tree
        for i in range(0, height) :
            print(" " * (height - i), end = "")
            print("o" * (2*i + 1))

        # print tree trunk
        for i in range(0, int(height / 3)):
            print (" " * int((2*height + 1)/2), end = "")
            print("o")

        return
>>>>>>> 0e9345cda92eb5709818714a905c011dfd8d30ce
