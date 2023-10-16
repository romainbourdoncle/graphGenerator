import random
import subprocess
import os

n_vertices = 456 #number of vertices
p_edge = 0.008  #probability of an edge between any pair of vertices

#generate random coordinates for vertices
vertices = [(random.uniform(0, 20), random.uniform(0, 20)) for _ in range(n_vertices)]

#each edge included in the graph with probability p, independently from every other edge
edges = set()
for i in range(n_vertices):
    for j in range(i+1, n_vertices):  # Avoid self-loops by starting from i+1
        if random.uniform(0, 1) < p_edge:
            edges.add((i, j))

#print resulting graph in TikZ format
tikz_code = "\\begin{tikzpicture}\n"

for x, y in vertices:
    tikz_code += f"\\node[draw, circle, fill=black, scale=0.5] at ({x}, {y}) {{}};\n"

for v1, v2 in edges:
    x1, y1 = vertices[v1]
    x2, y2 = vertices[v2]
    tikz_code += f"\\draw ({x1}, {y1}) -- ({x2}, {y2});\n"

tikz_code += "\\end{tikzpicture}"

#create LaTeX standalone doc
latex_document = (
    "\\documentclass{standalone}\n"
    "\\usepackage{tikz}\n"
    "\\begin{document}\n"
    f"{tikz_code}\n"
    "\\end{document}"
)

base_filename = f"G({n_vertices},{p_edge})_randomgraph"
filename = base_filename
counter = 1
while os.path.exists(filename + ".tex") or os.path.exists(filename + ".pdf"):
    filename = f"{base_filename}{counter}"
    counter += 1

filename_with_extension = filename + ".tex"
with open(filename_with_extension, "w") as file:
    file.write(latex_document)

#compile to PDF
try:
    subprocess.run(["pdflatex", filename_with_extension], check=True)
    print(f"\nThe file {filename_with_extension} has been successfully compiled to PDF.")
    print(f"You can open {filename}.pdf to view the generated graph.")
except subprocess.CalledProcessError:
    print("\nAn error occurred while compiling the .tex file to PDF.")
    print("Make sure that pdflatex is installed and available in your PATH.")
