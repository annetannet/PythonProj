#!/usr/bin/env python3

import bfs
import dfs
import dikstra
import top_sort
import top_sort_DFS
import unittest


class TestGraphs(unittest.TestCase):
    def test_bfs_simple_graph(self):
        self.assertEqual(bfs.BFS([[1, 2], [0, 2], [0, 1, 3], [2]], 0), [0, 1, 2, 3])
        self.assertEqual(bfs.BFS([[1, 2, 3, 4, 5], [0], [0], [0], [0], [4]], 0), [0, 1, 2, 3, 4, 5])

    def test_bfs_directed_graph(self):
        self.assertEqual(bfs.BFS([[1, 2], [0, 2], [1]], 0), [0, 1, 2])
        self.assertEqual(bfs.BFS([[1, 2], [0, 2], [1]], 1), [1, 0, 2])
        self.assertEqual(bfs.BFS([[1, 2], [0, 2], [1]], 2), [2, 1, 0])

    def test_bfs_non_incident_nodes(self):
        self.assertEqual(bfs.BFS([[], [], [], []], 0), [0])
        self.assertEqual(bfs.BFS([[1, 2, 3], [], [], []], 1), [1])
        self.assertEqual(bfs.BFS([[1, 2, 3], [], [], []], 2), [2])
        self.assertEqual(bfs.BFS([[1, 2, 3], [1, 2, 3], [1, 2, 3], []], 3), [3])

    def test_bfs_empty_graph(self):
        self.assertEqual(bfs.BFS([], 0), [])
        self.assertEqual(bfs.BFS([], 1), [])
        self.assertEqual(bfs.BFS([], 2), [])

    def test_bfs_node_out_of_graph(self):
        self.assertEqual(bfs.BFS([[1, 20000], [0, 2], [0, 1, 3], [2]], 0), [])  # The node 20000 out of graph
        self.assertEqual(bfs.BFS([[1, 2, 3, 4, 5], []], 0), [])  # The node 2 out of graph
        self.assertEqual(bfs.BFS([[1], []], 10), [])  # The node 10 out of graph

    def test_dfs_empty_graph(self):
        self.assertEqual(dfs.DFS([], 10), [])

    def test_dfs_simple_graph(self):
        self.assertEqual(dfs.DFS([[1, 2], [3, 4], [], [], []], 0), [0, 1, 3, 4, 2])

    def test_dfs_common_graph(self):
        self.assertEqual(dfs.DFS(
            [[1, 2], [3, 4], [0, 1], [], [5, 6], [], [7, 8], [], []], 0),
            [0, 1, 3, 4, 5, 6, 7, 8, 2])

    def test_dfs_node_out_of_graph(self):
        self.assertEqual(dfs.DFS([[1, 2], [3, 4], [], [], []], 10), [])  # The node 10 out of graph
        self.assertEqual(dfs.DFS([[1, 2], [3, 4], [1], [1]], 0), [0, 1, 3, 2])  # The node 4 out of graph

    def test_dfs_no_repetition_visits(self):
        self.assertEqual(dfs.DFS([[1, 2], [3, 4], [1], [1], [0]], 0), [0, 1, 3, 4, 2])
        self.assertEqual(dfs.DFS([[1, 2], [3, 4], [0], [1], [1]], 0), [0, 1, 3, 4, 2])

    def test_dfs_cycle(self):
        self.assertEqual(dfs.DFS([[1], [2], [0]], 0), [0, 1, 2])

    def test_top_sort_empty_graph(self):
        self.assertEqual(top_sort.TopologicalSort([]), [])

    def test_top_sort_node_out_of_graph(self):
        self.assertEqual(top_sort.TopologicalSort([[1, 2], [3], []]), [])  # The node 3 out of graph
        self.assertEqual(top_sort.TopologicalSort([[1, 2]]), [])  # The node 1 out of graph
        self.assertEqual(top_sort.TopologicalSort([[1, 2, 10], [], []]), [])  # The node 10 out of graph

    def test_common_topological_sort(self):
        self.assertEqual(top_sort.TopologicalSort([[1, 2], [3, 4], [3, 4], [5], [5], []]), [0, 2, 1, 4, 3, 5])

    def test_empty_graph_Dijkstra(self):
        self.assertEqual(dikstra.Dijkstra([], ()), [])

    def test_Dijkstra_common(self):
        self.assertEqual(dikstra.Dijkstra([[(1, 1), (2, 2)], [(3, 3)], [(3, 3)], []], (0, 0)), [0, 1, 2, 4])
        self.assertEqual(dikstra.Dijkstra([[(1, 1), (2, 2), (3, 3)], [(3, 3)], [(3, 3)], []], (0, 0)), [0, 1, 2, 3])

    def test_top_sort_DFS(self):
        self.assertEqual(top_sort_DFS.DFS([[1, 2], [2], []]), [0, 1, 2])
        self.assertEqual(top_sort_DFS.DFS([[1, 2], [2], [3], []]), [0, 1, 2, 3])

    def test_top_sort_DFS_empty_graph(self):
        self.assertEqual(top_sort_DFS.DFS([]), [])

    def test_top_sort_DFS_node_out_of_graph(self):
        self.assertEqual(top_sort_DFS.DFS([[1, 4], [4], []]), [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
