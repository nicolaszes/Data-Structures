# 递归DFS
def depth_first_search(self, root = None):
    order = []
    def dfs(node):
        self.visited[node] = True
        order.append(node)
        for n in self.node_neighbors[node]:
            if not n in self.visited:
                dfs(n)

    if root:
        dfs(root)

    # 对于不连通的结点（即dfs（root）完仍是没有visit过的单独处理，再做一次dfs
    for node in self.nodes():
        if not node in self.visited:
            dfs(node)
    self.visited = {}
    print(order)
    return order

# 非递归DFS
def depth_first_search2(self, root = None):
    stack = []
    order = []
    # self.visited[root] = True
    def dfs():
        while stack:
            node = stack[-1]
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    order.append(n)
                    stack.append(n)
                    self.visited[n] = True
                    break
            else:
                stack.pop()
    if root:
        stack.append(root)
        order.append(root)
        self.visited[root]=True
        dfs()

    for node in self.nodes():
        if node not in self.visited:
            stack.append(node)
            order.append(node)
            self.visited[node]=True
            dfs()

    self.visited = {}
    print(order)
    return order