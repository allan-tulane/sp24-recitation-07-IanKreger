from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
      current = frontier.pop()
      for neighbor in graph[current]:
        if neighbor not in result:
          result.add(neighbor)
          frontier.add(neighbor)
    return result
    




def connected(graph):
  if len(graph) == 0:
    return False
  start = next(iter(graph.keys()))
  r_nodes = reachable(graph, start)
  if len(r_nodes) == len(graph):
    return True
  else:
    return False
  
    
  



def n_components(graph):
  count = 0
  vis_nodes = set()
  for node in graph:
    if node not in vis_nodes:
      count +=1
      vis_nodes.update(reachable(graph, node))
  return count

