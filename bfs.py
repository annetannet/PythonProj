from collections import deque


def BFS(graph, start):
    """
    Обход графа в ширину
    :param graph: список вершин графа, каждая вершина(элемент списка) содержит список вершин, с которыми инцидентна
    :param start: вершина, с которой начинается обход графа
    :return: список вершин, в той последовательности, в которой BFS проходит по графу
    """
    # Проверка, не пустой ли граф
    if len(graph) == 0:
        return []
    # Проверка корректности номера вершины
    if start >= len(graph):
        print(f'The node {start} out of graph')
        return []

    deq = deque()  # Создаём очередь для хранения вершин, в которые можно попасть
    result = list()
    deq.append(start)
    used = [False] * len(graph)  # Создаём список посещений вершин: True - вершину посетили, False - нет
    used[start] = True
    # Пока есть вершины, в которые можно попасть, будет осуществляться обход графа
    while len(deq) > 0:
        point_now = deq.popleft()  # Добавление текущей вершины в список
        result.append(point_now)
        for i in graph[point_now]:  # Проход по всем вершинам, инцидентным текущей
            # Проверка корректности номера вершины
            if i >= len(graph):
                print(f'The node {i} out of graph')
                return []
            if not used[i]:  # Если вершина ещё не была посещена, добавляем её в конец очереди
                deq.append(i)
                used[i] = True
    return result
