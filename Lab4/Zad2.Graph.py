class Vertex:
    def __init__(self, names='', edges=0):
        self.name = names
        self.edges = {}
        for i, j in names, edges:
            self.edges[i] = j

    def __repr__(self):
        return 'Vertex {} with edges {}'.format(self.name, self.edges)


class Edge:
    def __init__(self, start, end, cost=1, visited=False):
        self.start = start
        self.end = end
        self.cost = cost
        self.visited = visited

    def __repr__(self):
        return 'Edge with start {}, end {}, cost {}, visited {}'.format(self.start, self.end, self.cost, self.visited)


class SimpleGraph:
