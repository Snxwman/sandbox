class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:

        class UnionFind:
            def __init__(self, num_nodes: int, edges: list[list[int]]) -> None:
                self.parent: list[int] = list(range(num_nodes))
                self.rank: list[int] = [1] * num_nodes
                self.min_cost: list[int] = [-1] * num_nodes

                for node_u, node_v, weight in edges:
                    self.union(node_u, node_v, weight)


            def union(self, node_u: int, node_v: int, weight: int) -> None:
                rep_u = self.find(node_u)
                rep_v = self.find(node_v)

                if rep_u == rep_v:
                    self.min_cost[rep_u] &= weight
                    return

                if self.rank[rep_u] > self.rank[rep_v]:
                    self.parent[rep_v] = rep_u
                    self.rank[rep_u] += 1
                    self.min_cost[rep_u] &= weight & self.min_cost[rep_v]
                else:
                    self.parent[rep_u] = rep_v
                    self.rank[rep_v] += 1
                    self.min_cost[rep_v] &= weight & self.min_cost[rep_u]


            def find(self, node: int) -> int:
                if self.parent[node] != node:
                    self.parent[node] = self.find(self.parent[node])

                return self.parent[node]


        uf = UnionFind(n, edges)
        answer: list[int] = []

        for source, target in query:
            if source == target:
                answer.append(0)
            elif uf.find(source) != uf.find(target):
                answer.append(-1)
            else:
                answer.append(uf.min_cost[uf.find(source)])

        return answer

