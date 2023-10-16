import random

n_vertices = 456 #number of vertices
p_edge = 0.008  #probability of an edge between any pair of vertices

#generate random coordinates for vertices
vertices = [(random.uniform(0, 20), random.uniform(0, 20)) for _ in range(n_vertices)]

#each edge included in the graph with probability p, independently from every other edge
edges = set()
for i in range(n_vertices):
    for j in range(i+1, n_vertices):  #avoid self-loops by starting from i+1
        if random.uniform(0, 1) < p_edge:
            edges.add((i, j))

#print resulting graph in TikZ format
print("\\begin{tikzpicture}")

for x, y in vertices:
    print(f"\\node[draw, circle, fill=black, scale=0.5] at ({x}, {y}) {{}};")

for v1, v2 in edges:
    x1, y1 = vertices[v1]
    x2, y2 = vertices[v2]
    print(f"\\draw ({x1}, {y1}) -- ({x2}, {y2});")

print("\\end{tikzpicture}")
