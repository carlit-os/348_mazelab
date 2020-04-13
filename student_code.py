import common


# global vars
# length = 0
# width = 0


# object def for a spot in the maze
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_start(atlas):
    for rdx, row in enumerate(atlas):
        for cdx, num in enumerate(row):
            if num == 2:
                result = Node(rdx, cdx)
                return result


def in_range(x, y, length, width):
    return 0 <= x < length and 0 <= y < width


def expand(curr_node, atlas, length, width):
    atlas[curr_node.x][curr_node.y] = 4  # this expanded node needs to get marked

    candidates = []

    curr_node.x = curr_node.x + 1
    candidates.append([curr_node.x, curr_node.y])  # space below of currnode
    print("checking below")
    print(candidates[0][0])
    print(candidates[0][1])

    curr_node.y = curr_node.y - 1
    curr_node.x = curr_node.x - 1
    candidates.append([curr_node.x, curr_node.y])  # space left of currnode
    print("checking left")
    print("indexed atlas[%d][%d]" % (curr_node.x, curr_node.y))

    curr_node.y = curr_node.y + 1
    curr_node.x = curr_node.x - 1
    candidates.append([curr_node.x, curr_node.y])  # space above of currnode
    print("checking above")
    print("indexed atlas[%d][%d]" % (curr_node.x, curr_node.y))

    curr_node.x = curr_node.x + 1
    curr_node.y = curr_node.y + 1  # space right of currnode
    candidates.append([curr_node.x, curr_node.y])
    print("checking right")
    print("indexed atlas[%d][%d]" % (curr_node.x, curr_node.y))

    curr_node.y = curr_node.y - 1  # set currnode back where it belongs
    print("left currnode at atlas[%d][%d]" % (curr_node.x, curr_node.y))

    print("candidates are")
    print(candidates)
    viable = list(filter(
        lambda candidate: in_range(candidate[0], candidate[1], length, width) and atlas[candidate[0]][
            candidate[1]] == 0,
        candidates))

    print("we're left with")
    print(viable)
    return map(lambda candidate: Node(candidate[0], candidate[1]), viable)

    # for candidate in candidates:#candidate is a potential set of surrounding coords
    #  if x<width and y<length and map[candidate[0]][candidate[1]] != 1:#within bounds and not a wall
    #    result.app


def deep_walker(curr_node, atlas, width, length):
    print("indexing")
    print(curr_node.x, curr_node.y)
    print(atlas[curr_node.x][curr_node.y])

    # print("indexing atlas[8],[10]")
    # print(atlas[curr_node.y][curr_node.x]) # this goes out of range

    if atlas[curr_node.x][curr_node.y] == 3:
        atlas[curr_node.x][curr_node.y] = 5
        return True
    for step in expand(curr_node, atlas, width, length):

        if deep_walker(step, atlas, width, length):
            atlas[curr_node.x][curr_node.y] = 5
            return deep_walker(step, atlas, width, length)
    return False


def df_search(atlas):
    found = False
    # PUT YOUR CODE HERE
    # access the map using "map[y][x]"
    # y between 0 and common.constants.MAP_HEIGHT-1
    # x between 0 and common.constants.MAP_WIDTH-1

    # use a list as a stack
    # get start coords
    start_node = find_start(atlas)

    # get dimensions of map
    width = len(atlas)
    length = len(atlas[0])

    # print("starting at")
    # rint(start_node.x)
    # print(start_node.y)
    # frontier = (expand(start_node, atlas,length,width))
    # print("expanded to nodes")
    # print(frontier[0].x, frontier[0].y)
    # print("and")
    # print(frontier[1].x, frontier[1].y)
    found = deep_walker(start_node, atlas, width, length)

    return found


def bf_search(atlas):
    found = False;
    # PUT YOUR CODE HERE
    # access the map using "map[y][x]"
    # y between 0 and common.constants.MAP_HEIGHT-1
    # x between 0 and common.constants.MAP_WIDTH-1
    return found
