# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Node:
    def __init__(self, y, x):
        self.X = x
        self.Y = y

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y


def bfs(dimension, start, end):
    moves = 0
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)
    while queue:
        currentnode = queue.pop(0)


        # Left Move
        Lneighbour = Node(currentnode.Y, currentnode.X)
        Lneighbour.X = Lneighbour.X - 1

        if (Lneighbour.X > 0) and (maze[Lneighbour.Y - 1][Lneighbour.X - 1] == 1):
            if Lneighbour not in visited:
                queue.append(Lneighbour)
                visited.append(Lneighbour)

        # Right Move
        Rneighbour = Node(currentnode.Y, currentnode.X)
        Rneighbour.X = Rneighbour.X + 1
        if (Rneighbour.X <= dimension) and (maze[Rneighbour.Y - 1][Rneighbour.X - 1] == 1):
            if Rneighbour not in visited:
                queue.append(Rneighbour)
                visited.append(Rneighbour)

        # Up Move
        Uneighbour = Node(currentnode.Y, currentnode.X)
        Uneighbour.Y = Uneighbour.Y - 1
        if (Uneighbour.Y > 0) and (maze[Uneighbour.Y - 1][Uneighbour.X - 1] == 1):
            if Uneighbour not in visited:
                queue.append(Uneighbour)
                visited.append(Uneighbour)

        # Down Move
        Dneighbour = Node(currentnode.Y, currentnode.X)
        Dneighbour.Y = Dneighbour.Y + 1
        if (Dneighbour.Y <= dimension) and (maze[Dneighbour.Y - 1][Dneighbour.X - 1] == 1):
            if Dneighbour not in visited:
                queue.append(Dneighbour)
                visited.append(Dneighbour)

        if currentnode == end:
            break
        if currentnode != start:
            moves += 1

    print("It took me ", moves, "in BFS :\n")


def dfs(dimension, start, end):
    moves = 1
    visited = []
    dfsrec(dimension, start, end, moves, visited)


def dfsrec(dimension, start, end, moves, visited, Found=False):
    visited.append(start)
    if start == end:
        Found = True
        print("It took me ", moves, "in DFS :\n")
        # Left Move
    Lneighbour = Node(start.Y, start.X)
    Lneighbour.X = Lneighbour.X - 1
    if not Found:
        if (Lneighbour.X > 0) and (maze[Lneighbour.Y - 1][Lneighbour.X - 1] == 1):
            if Lneighbour not in visited:
                moves += 1
                dfsrec(dimension, Lneighbour, end, moves, visited, Found)

    if not Found:

        # Right Move
        Rneighbour = Node(start.Y, start.X)
        Rneighbour.X = Rneighbour.X + 1
        if (Rneighbour.X <= dimension) and (maze[Rneighbour.Y - 1][Rneighbour.X - 1] == 1):
            if Rneighbour not in visited:
                moves += 1

                dfsrec(dimension, Rneighbour, end, moves, visited, Found)

    if not Found:

        # Up Move
        Uneighbour = Node(start.Y, start.X)
        Uneighbour.Y = Uneighbour.Y - 1
        if (Uneighbour.Y > 0) and (maze[Uneighbour.Y - 1][Uneighbour.X - 1] == 1):
            if Uneighbour not in visited:
                moves += 1

                dfsrec(dimension, Uneighbour, end, moves, visited, Found)
    if not Found:

        # Down Move
        Dneighbour = Node(start.Y, start.X)
        Dneighbour.Y = Dneighbour.Y + 1
        if (Dneighbour.Y <= dimension) and (maze[Dneighbour.Y - 1][Dneighbour.X - 1] == 1):
            if Dneighbour not in visited:
                moves += 1

                dfsrec(dimension, Dneighbour, end, moves, visited, Found)

    if not Found:
        moves -= 1
    return


def main():
    dimensions = 12
    startpoint = Node(5, 12)
    endpoint = Node(11, 1)
    bfs(dimensions, startpoint, endpoint)
    dfs(dimensions, startpoint, endpoint)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
