import functools
import time
import dfs
import bfs
import dikstra
import top_sort
import top_sort_DFS
import graph_generator
import copy


def logging(function):
    @functools.wraps(function)
    def wrapper(*args):
        N = 1000
        function(*args)
        function(*args)
        start_time = time.time()
        for _ in range(N):
            function(*args)
        end_time = time.time()
        work_time = end_time - start_time
        print(work_time / N, end="\n\n")

    return wrapper


@logging
def speed_dfs(graph, start):
    return dfs.DFS(graph, start)


@logging
def speed_bfs(a, start):
    return bfs.BFS(a, start)


@logging
def speed_top_sort_Kahn(a):
    return top_sort.TopologicalSort(a)


@logging
def speed_top_sort_DFS(a):
    return top_sort_DFS.DFS(a)


@logging
def speed_dijkstra(a, start):
    return dikstra.Dijkstra(a, start)


if __name__ == '__main__':
    best_data_8KB = graph_generator.best_graph(900)
    worst_data_8KB = graph_generator.worst_graph(45)
    rnd_data_4KB = graph_generator.random_graph(75)
    best_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.best_graph(550), 2)
    worst_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.worst_graph(30), 2)
    rnd_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.random_graph(50), 2)
    print("DFS")
    speed_dfs(best_data_8KB, 0)
    speed_dfs(worst_data_8KB, 0)
    speed_dfs(rnd_data_4KB, 0)
    print("BFS")
    speed_bfs(best_data_8KB, 0)
    speed_bfs(worst_data_8KB, 0)
    speed_bfs(rnd_data_4KB, 0)
    print("Topological sort by Kahn")
    speed_top_sort_Kahn(best_data_8KB)
    speed_top_sort_Kahn(worst_data_8KB)
    speed_top_sort_Kahn(rnd_data_4KB)
    print("Topological sort on DFS")
    speed_top_sort_DFS(best_data_8KB)
    speed_top_sort_DFS(worst_data_8KB)
    speed_top_sort_DFS(rnd_data_4KB)
    print("Dijkstra")
    speed_dijkstra(best_weighted_graph_8KB, (0, 0))
    speed_dijkstra(worst_weighted_graph_8KB, (0, 0))
    speed_dijkstra(rnd_weighted_graph_8KB, (0, 0))
