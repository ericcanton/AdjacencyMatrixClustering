import numpy as np

from graph.disjoint_set import DisjointSet


class AdjacencyMatrix:
    def __init__(self, matrix: np.ndarray):
        self.matrix = matrix

    def find_clusters(self, threshold: float) -> DisjointSet:
        pass