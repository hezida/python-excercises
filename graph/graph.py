import json

with open('input') as f:
  graph = {}
  for line in f:
    line=line.rstrip()
    line_data = line.split(":")
    source_vertices = line_data[0].split(",")
    target_vertices = line_data[1].split(",")
    for s in source_vertices:
      if s not in graph:
        graph[s] = set()
      for t in target_vertices:
        graph[s].add(t)
        #if t not in graph:
        #  graph[t] = set()
        #graph[t].add(s)

# post processing of the graph
set_to_add=set()
for v in graph:
  for u in graph[v]:
    if u not in graph:
      set_to_add.add(u)
for s in set_to_add:
  graph[s] = set()

print(graph)
not_visited = set(graph.keys())
circle=False
stop=False
while not_visited:
  to_visit = set()
  node = not_visited.pop()
  not_visited.add(node)
  to_visit.add(node)
  while to_visit:
    node = to_visit.pop()
    if node in not_visited:
      not_visited.remove(node)
      to_visit.update(graph[node])
    else:
      circle=True
      break
  else:
    break

print(circle)