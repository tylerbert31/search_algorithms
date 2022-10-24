from queue import PriorityQueue

verticelist = {
    'a': {},
    'b': {'a': 2},
    'c': {'a': 2},
    'd': {'b': 1, 'c': 8, 'e': 2},
    'e': {'h': 8, 'r': 2},
    'f': {'c': 3, 'g': 2},
    'g': {},
    'h': {'p': 4, 'q': 4},
    'p': {'q': 15},
    'q': {},
    'r': {'f': 2},
    's': {'d': 3, 'e': 9, 'p': 1}
}


def ucs(graph, source, destination):
    expanded = []
    q = PriorityQueue()
    q.put((0, source))
    visited = set()

    while q:

        weight, vertex = q.get()
        current = vertex[-1] 

        if current not in visited: 
            visited.add(current)
            expanded.append(
                current) 

            if current == destination:  
                return vertex, expanded

            children = graph[current]  
            for i in children:
                if i not in visited: 
                    totalweight = weight + children[i]
                    q.put((totalweight,
                           vertex + i))  


solution, expanded = ucs(verticelist, 's', 'g')
print('The return path is ----> ', solution)
print("The expanded vertex list until reaching the destination is ---->", expanded)