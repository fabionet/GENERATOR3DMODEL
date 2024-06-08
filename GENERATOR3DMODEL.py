import numpy as np
from stl import mesh

# Approximate dimensions of the mouse
length = 115.0  # mm
width = 65.0  # mm
height = 40.0  # mm

# Define the coordinates for the vertices of a simplified mouse model
vertices = np.array([
    [0, 0, 0],
    [length, 0, 0],
    [length, width, 0],
    [0, width, 0],
    [0, 0, height],
    [length, 0, height],
    [length, width, height],
    [0, width, height]
])

# Define the faces of the simplified mouse model
faces = np.array([
    [0, 1, 2],
    [0, 2, 3],
    [4, 5, 6],
    [4, 6, 7],
    [0, 1, 5],
    [0, 5, 4],
    [1, 2, 6],
    [1, 6, 5],
    [2, 3, 7],
    [2, 7, 6],
    [3, 0, 4],
    [3, 4, 7]
])

# Create the mesh
mouse_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        mouse_mesh.vectors[i][j] = vertices[f[j], :]

# Save the mesh to file
stl_path = "mouse_model.stl"
mouse_mesh.save(stl_path)

