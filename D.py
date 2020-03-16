"""wg forge task-D"""
# !/usr/bin/python2
import sys

from copy import copy


class Vertex:
    """Class for create vertex graph obj"""

    def __init__(self, node):
        self.id = node
        self.connections = {}

    def add_neighbor(self, neighbor, weight=1):
        """Add connection on vertex"""
        self.connections[neighbor] = weight

    def get_connections(self):
        """Return vertex connection names"""
        return self.connections.keys()

    def get_id(self):
        """Return vertex name(id)"""
        return self.id

    def get_weight(self, neighbor):
        """Get weight by connection name"""
        return self.connections[neighbor]


class Graph:
    """Graph entity"""

    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, node):
        """Add vertex in graph"""
        self.num_vertices += 1
        vertex = Vertex(node)
        self.vert_dict[node] = vertex
        return node

    def get_vertex(self, node):
        """Get vertex by node"""
        if node in self.vert_dict:
            return self.vert_dict[node]
        return None

    def add_edge(self, frm, to, weight=0):
        """Add two board connection in graph"""
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(to, weight)
        self.vert_dict[to].add_neighbor(frm, weight)

    def get_vertices(self):
        """return vertex indexes(nodes)"""
        return self.vert_dict.keys()


def fill_graph(graph, index, input_vertex_node):
    """Fill solution graph with recursion uses input vertex"""
    next_index = index + 1
    while next_index < len(INPUT_RANGES):
        next_element = INPUT_RANGES[next_index]
        if (next_element - INPUT_RANGES[index]) > HOURS_OF_SHIFT:
            next_index += 1
            continue

        output_vertex_node = graph.add_vertex(graph.num_vertices)

        graph.add_edge(
            input_vertex_node,
            output_vertex_node,
            next_element - INPUT_RANGES[index]
        )

        fill_graph(graph, next_index, output_vertex_node)

        next_index += 1


def find_shift_count(graph, input_vertex_node, weights):
    """Find all solustions with different shift distribution"""
    vertex_connections = graph.get_vertex(input_vertex_node).connections
    if len(vertex_connections) == 1:
        if (sum(weights[i] for i in range(0, len(weights)) if not i % 2) == HOURS_OF_SHIFT and sum(
                weights[i] for i in range(0, len(weights)) if i % 2 == 1) == HOURS_OF_SHIFT):
            RESULT.append(len(weights) - 1)
            if 3 in RESULT:
                print('Yes')
                print(3)
                sys.exit(0)

    for node in sorted(list(vertex_connections)):
        if node < input_vertex_node:
            continue

        weights.append(vertex_connections[node])
        find_shift_count(graph, node, weights)
        weights.pop()


if __name__ == '__main__':
    HOURS_OF_SHIFT, COUNT_RANGES = map(int, raw_input().split(' '))

    INPUT_RANGES = [0]
    for _index in range(COUNT_RANGES):
        worked_range = raw_input().split(' ')
        worked_range = map(int, worked_range)
        worked_range[-1] += 1
        INPUT_RANGES += range(*worked_range)

    INPUT_RANGES.append(HOURS_OF_SHIFT * 2)

    if HOURS_OF_SHIFT in INPUT_RANGES:
        print('Yes')
        print(1)
        sys.exit(0)

    SUB = lambda x: x - HOURS_OF_SHIFT
    COPY_INPUT_RANGES = copy(INPUT_RANGES)
    COPY_INPUT_RANGES = map(SUB, COPY_INPUT_RANGES)
    if len(set(INPUT_RANGES).intersection(COPY_INPUT_RANGES)) > 0:
        print('Yes')
        print(2)
        sys.exit(0)

    GRAPH = Graph()
    INPUT_VERTEX_NODE = GRAPH.add_vertex(GRAPH.num_vertices)
    fill_graph(GRAPH, 0, INPUT_VERTEX_NODE)

    RESULT = []
    find_shift_count(GRAPH, 0, [])

    if not RESULT:
        print('No')
        sys.exit(0)
    else:
        print('Yes')
        print(min(RESULT))
        sys.exit(0)
