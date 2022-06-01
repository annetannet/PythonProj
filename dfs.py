def DFS(graph, node):
    """
    Обход графа в глубину
    :param graph: граф
    :param node: текущая вершина
    :return: упорядоченный список вершин, по которому алгоритм проходит граф
    """
    # Проверка, не пустой ли граф
    if len(graph) == 0:
        return []
    used = {}  # Словарь, ключи которого - вершины,
    # Значение ключа True, если вершину посетили
    # False в противном случае
    ans = []  # Порядок вершин, в котором проходим по графу

    def dfs(graph, node):  # Сам алгоритм поиска в глубину

        # Проверка корректности номера вершины
        if node >= len(graph):
            print(f'The node {node} out of graph')
            return []

        used[node] = True
        ans.append(node)
        for i in graph[node]:
            if not used.get(i):  # Проверяем, если уже были в i-ой вершине, второй раз не идём
                dfs(graph, i)

    dfs(graph, node)
    return ans
