class Vertex:
    def __init__(self, names='', edges=None):
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
    def __init__(self, verts=[], edges=[]):
        pass

    def __repr__(self):
        pass

    def add_vertex(v):
        pass

    def add_edge(v_1, v_2):
        pass

    def contains_vertex(v):
        pass

    def contains_edge(v_1, v_2):
        pass

    def get_neighbors(v):
        pass

    def is_empty():
        pass

    def size():
        pass

    def remove_vertex(v):
        pass

    def remove_edge(v_1, v_2):
        pass

    def is_neighbor(v1, v2):
        pass

    def is_reachable(v1, v2):
        pass

    def clear_all():
        pass


if __name__ == '__main__':

