"""wg forge task-D"""
#!/usr/bin/python2
import sys

from IPython import embed

class Vertex:
    def __init__(self, node):
        self.id = node
        self.connections = {}

    def add_neighbor(self, neighbor, weight=1):
        self.connections[neighbor] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connections[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return node

    def get_vertex(self, node):
        if node in self.vert_dict:
            return self.vert_dict[node]
        else:
            return None

    def add_edge(self, frm, to, weight=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(to, weight)
        self.vert_dict[to].add_neighbor(frm, weight)

    def get_vertices(self):
        return self.vert_dict.keys()


class Girl:
    worked = []

    @classmethod
    def clean_worked_list(cls):
        cls.worked = []

    def __init__(self, name):
        self.name = name
        self.worked_hours = []

    def add_hours(self, count):
        self.worked_hours.append(count)

    def get_sum_hours(self):
        return sum(self.worked_hours)


if __name__ == '__main__':
    HOURS_OF_SHIFT, COUNT_RANGES = map(int, raw_input().split(' '))

    INPUT_RANGES = [0]
    for index in range(COUNT_RANGES):
        worked_range = raw_input().split(' ')
        worked_range = map(int, worked_range)
        worked_range[-1] += 1
        INPUT_RANGES += range(*worked_range)

    INPUT_RANGES.append(HOURS_OF_SHIFT * 2)

    graph = Graph()
    input_vertex = graph.add_vertex(graph.num_vertices)
    for index, element in enumerate(INPUT_RANGES):
        next_index = index + 1
        while next_index < len(INPUT_RANGES):
            output_vertex = graph.add_vertex(graph.num_vertices)
            next_element = INPUT_RANGES[next_index]

            graph.add_edge(
                input_vertex, 
                output_vertex, 
                next_element - element
            )

            next_index += 1

        input_vertex = output_vertex

    print(graph.get_vertices())
