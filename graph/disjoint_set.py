
class DisjointSetNode:
    def __init__(self, id: str):
        self.id = id
        self.rank = 0
        self.parent = self

class DisjointSet:
    def __init__(self, elements: list = []):
        self.elements = set(elements)

    def make_set(self, vertex: DisjointSetNode) -> None:
        """
        Adds `vertex` to `self.elements` and `{vertex}` to the set partition... if not already in there.
        :param vertex: Add this, or do nothing if already in `self.elements`.
        :return: `None`
        """
        if vertex not in self.elements:
            self.elements.add(vertex)
            vertex.parent = vertex
            vertex.rank = 0

    def find(self, vertex: DisjointSetNode) -> DisjointSetNode:
        """
        Path compression algorithm. Makes star-shaped trees.
        :param vertex: The vertex whose root will be found and set to vertex.parent.
                       Not required to be a member of this `DisjointSet`
        :return: The root of `vertex`.
        """
        if vertex.parent != vertex:
            vertex.parent = self.find(vertex.parent)
            return vertex.parent
        else:
            return vertex

    def union(self, vertexA: DisjointSetNode, vertexB: DisjointSetNode) -> None:
        a = self.find(vertexA)
        b = self.find(vertexB)

        if a == b: return

        if a.rank < b.rank:
            a, b = b, a

        b.parent = a
        if a.rank == b.rank:
            a.rank += 1
