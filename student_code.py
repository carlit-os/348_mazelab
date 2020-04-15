import common


# object def for a spot in the maze
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_start(atlas, frontier):  # finds start node, adds to frontier, marks with 5
    for rdx, row in enumerate(atlas):
        for cdx, num in enumerate(row):
            if num == 2:
                result = Node(rdx, cdx)

                atlas[result.x][result.y] = 5
                frontier.append(result)

                return result


def in_range(x, y):  # checks if node is inside of the atlas
    return 0 <= x <= (common.constants.MAP_HEIGHT - 1) and 0 <= y <= (common.constants.MAP_WIDTH - 1)


def trace(curr_node, parent, atlas):
    # curr_node is the goal node

    while parent[curr_node.x][curr_node.y] != 0:  # while we haven't gotten back to start

        parentx = parent[curr_node.x][curr_node.y][0]  # previous coordinates
        parenty = parent[curr_node.x][curr_node.y][1]

        atlas[parentx][parenty] = 5  # breadtrail of correct path
        curr_node = Node(parentx, parenty)


def expand(curr_node, atlas):  # returns a list of 0 nodes counterclockwise from right of curr
    print("indexing atlas[%d][%d]" % (curr_node.x, curr_node.y))
    candidates = []

    curr_node.x = curr_node.x - 1
    candidates.append([curr_node.x, curr_node.y])  # space above of currnode
    print("checking right")
    print("indexed atlas[%d][%d]" % (curr_node.x, curr_node.y))

    curr_node.y = curr_node.y - 1
    curr_node.x = curr_node.x + 1  # space left of currnode
    candidates.append([curr_node.x, curr_node.y])
    print("checking above")
    print("indexed atlas[%d][%d]" % (curr_node.x, curr_node.y))

    curr_node.y = curr_node.y + 1
    curr_node.x = curr_node.x + 1
    candidates.append([curr_node.x, curr_node.y])  # space below currnode
    print("checking left")
    print("indexed atlas[%d][%d]" % (curr_node.x, curr_node.y))

    curr_node.x = curr_node.x - 1
    curr_node.y = curr_node.y + 1  # space right of currnode
    candidates.append([curr_node.x, curr_node.y])
    print("checking right")
    print("indexed atlas[%d][%d]" % (curr_node.x, curr_node.y))

    curr_node.y = curr_node.y - 1  # set currnode back where it belongs
    print("left currnode at atlas[%d][%d]" % (curr_node.x, curr_node.y))

    print("candidates are")
    print(candidates)
    viable = list(filter(
        lambda candidate: in_range(candidate[0], candidate[1]) and (atlas[candidate[0]][candidate[1]] == 0 or
                                                                    atlas[candidate[0]][candidate[1]] == 3),
        candidates))

    print("we're left with")
    print(viable)

    return list(map(lambda candidate: Node(candidate[0], candidate[1]), viable))


def df_search(atlas):
    found = False

    frontier = []
    # use a list as a stack
    parent = [[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]

    start_node = find_start(atlas, frontier)  # add to frontier and mark visited

    while frontier:
        curr_node = frontier.pop()
        if atlas[curr_node.x][curr_node.y] != 3:
            if curr_node is not start_node:
                atlas[curr_node.x][curr_node.y] = 4  # mark as visited
            for child in expand(curr_node, atlas):
                frontier.append(child)  # place child in frontier

                parent[child.x][child.y] = [curr_node.x, curr_node.y]
                # adds back trace to parent arr
        else:
            # parent[child.x][child.y] = [curr_node.x, curr_node.y]
            atlas[curr_node.x][curr_node.y] = 5
            trace(curr_node, parent, atlas)  # draw line of fives
            return True
    atlas[start_node.x][start_node.y] = 4  # there's no goal path
    return found


def bf_search(atlas):
    found = False
    # PUT YOUR CODE HERE
    # access the map using "map[y][x]"
    # y between 0 and common.constants.MAP_HEIGHT-1
    # x between 0 and common.constants.MAP_WIDTH-1
    return found
