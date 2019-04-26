def breadth_first_search(self, graph, start,  end):
  queue = []
  queue.append([start])
  self.visited.add(start)

  while queue:
    node = queue.pop()
    self.visited.add(node)

    self.process(node)
    nodes = self.generate_related_nodes(node)
    queue.push(nodes)

  # other processing work
  # ...