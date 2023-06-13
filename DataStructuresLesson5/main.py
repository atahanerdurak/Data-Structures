def dfs(graph, root):
    stack = []
    stack.append(root)
    discovered = [False] * len(graph.data)
    result = []
    while stack:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)
    return result


if not False:
    print("Hello")