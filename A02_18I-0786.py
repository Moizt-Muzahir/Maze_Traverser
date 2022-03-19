# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            Max = 0
            for i in range(len(self.queue)):
                if self.queue[i] >= self.queue[Max]:
                    Max = i
            item = self.queue[Max]
            del self.queue[Max]
            return item
        except IndexError:
            print()
            exit()

class PriorityStar(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            Max = 0
            for i in range(len(self.queue)):
                if self.queue[i] <= self.queue[Max]:
                    Max = i
            item = self.queue[Max]
            del self.queue[Max]
            return item
        except IndexError:
            print()
            exit()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Node:
    def __init__(self, y, x, cost, Dest=None):
        self.X = x
        self.Y = y
        self.cost = cost
        if Dest is None:
            self.Manhattan = 0
        else:
            self.Manhattan = (abs(self.X - Dest.X) + abs(self.Y - Dest.Y))

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def __lt__(self, other):
        return self.Manhattan < other.Manhattan

    def __le__(self, other):
        return self.Manhattan <= other.Manhattan

    def __gt__(self, other):
        return self.Manhattan > other.Manhattan

    def __ge__(self, other):
        return self.Manhattan >= other.Manhattan


def Astar(dimension, start, end):
    moves = 1

    queue = PriorityQueue()
    visited = []
    queue.insert(start)
    visited.append(start)
    while queue:
        currentnode = queue.delete()
        cost = currentnode.cost

        # Up Move
        Uneighbour = Node(currentnode.Y, currentnode.X, cost + 1, end)
        Uneighbour.Y = Uneighbour.Y - 1
        if (Uneighbour.Y > 0) and (maze[Uneighbour.Y - 1][Uneighbour.X - 1] == 1):
            if Uneighbour not in visited:
                queue.insert(Uneighbour)
                visited.append(Uneighbour)

        # Left Move
        Lneighbour = Node(currentnode.Y, currentnode.X, cost + 1, end)
        Lneighbour.X = Lneighbour.X - 1

        if (Lneighbour.X > 0) and (maze[Lneighbour.Y - 1][Lneighbour.X - 1] == 1):
            if Lneighbour not in visited:
                queue.insert(Lneighbour)
                visited.append(Lneighbour)

        # Right Move
        Rneighbour = Node(currentnode.Y, currentnode.X, cost + 1, end)
        Rneighbour.X = Rneighbour.X + 1
        if (Rneighbour.X <= dimension) and (maze[Rneighbour.Y - 1][Rneighbour.X - 1] == 1):
            if Rneighbour not in visited:
                queue.insert(Rneighbour)
                visited.append(Rneighbour)

        # Down Move
        Dneighbour = Node(currentnode.Y, currentnode.X, cost + 1, end)
        Dneighbour.Y = Dneighbour.Y + 1
        if (Dneighbour.Y <= dimension) and (maze[Dneighbour.Y - 1][Dneighbour.X - 1] == 1):
            if Dneighbour not in visited:
                queue.insert(Dneighbour)
                visited.append(Dneighbour)

        if currentnode == end:
            break
        if currentnode != start:
            moves += 1

    print("It took me ", moves, " moves in A* :\n")
    print("path cost ", currentnode.cost, "\n")


def BFS(dimension, start, end):
    moves = 1

    queue = PriorityStar()
    visited = []
    queue.insert(start)
    visited.append(start)
    while queue:
        currentnode = queue.delete()
        cost = currentnode.cost

        # Up Move
        Uneighbour = Node(currentnode.Y, currentnode.X, cost + 1, end)
        Uneighbour.Y = Uneighbour.Y - 1
        if (Uneighbour.Y > 0) and (maze[Uneighbour.Y - 1][Uneighbour.X - 1] == 1):
            if Uneighbour not in visited:
                queue.insert(Uneighbour)
                visited.append(Uneighbour)

        # Left Move
        Lneighbour = Node(currentnode.Y, currentnode.X, cost + 1, end)
        Lneighbour.X = Lneighbour.X - 1

        if (Lneighbour.X > 0) and (maze[Lneighbour.Y - 1][Lneighbour.X - 1] == 1):
            if Lneighbour not in visited:
                queue.insert(Lneighbour)
                visited.append(Lneighbour)

        # Right Move
        Rneighbour = Node(currentnode.Y, currentnode.X, cost + 1, end)
        Rneighbour.X = Rneighbour.X + 1
        if (Rneighbour.X <= dimension) and (maze[Rneighbour.Y - 1][Rneighbour.X - 1] == 1):
            if Rneighbour not in visited:
                queue.insert(Rneighbour)
                visited.append(Rneighbour)

        # Down Move
        Dneighbour = Node(currentnode.Y, currentnode.X, cost + 1, end)
        Dneighbour.Y = Dneighbour.Y + 1
        if (Dneighbour.Y <= dimension) and (maze[Dneighbour.Y - 1][Dneighbour.X - 1] == 1):
            if Dneighbour not in visited:
                queue.insert(Dneighbour)
                visited.append(Dneighbour)

        if currentnode == end:
            break
        if currentnode != start:
            moves += 1

    print("It took me ", moves, " moves in BFS :\n")
    print("path cost ", currentnode.cost, "\n")


def main():
    dimensions = 20
    endpoint = Node(13, 20, 0)
    startpoint = Node(15, 1, 0, endpoint)

    Astar(dimensions, startpoint, endpoint)
    BFS(dimensions, startpoint, endpoint)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
