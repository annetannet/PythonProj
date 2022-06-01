def TopologicalSort(graph):
    """

    Упорядочивание вершин ацикличного графа таким образом, что для любого ребра (u,v) номер вершины u меньше номера вершины v

    :param graph: ацикличный граф
    :return: список упорядоченных вершин
    """
    # Проверка, не пустой ли граф
    if len(graph) == 0:
        return []
    # Создать словарь степеней
    degree = dict()
    for node in range(len(graph)):
        degree[node] = 0
    # Получить степень каждого узла
    for node in graph:
        for connected_node in node:
            # Проверка корректности номера вершины
            if connected_node >= len(graph):
                print(f'The node {connected_node} out of graph')
                return []
            degree[connected_node] += 1
    # Добавить в список вершины со степенью 0
    nodes_zero_degree = [node for node in range(len(graph)) if degree[node] == 0]
    result = []
    # Выполняется при наличии элементов в списке
    while nodes_zero_degree:
        # Удалить последний элемент
        node = nodes_zero_degree.pop()
        # Сохранить полученную вершину в результате
        result.append(node)
        # Уменьшить степени всех вершин, на которые указывала удалённая
        for connected_node in graph[node]:
            degree[connected_node] -= 1
            # Если удаленная вершина (u) указывала на вершину степени 0 (v), v добавляется в очередь
            if degree[connected_node] == 0:
                nodes_zero_degree.append(connected_node)
    return result
