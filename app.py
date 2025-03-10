from scipy.optimize import root
from scipy.sparse.csgraph import connected_components, dijkstra, floyd_warshall, bellman_ford, depth_first_order
from scipy.optimize import minimize
from scipy.sparse import csr_matrix
from scipy.spatial import Delaunay
import numpy as np
from math import cos

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)

print(myroot.x)

def min_bfgs(x):
    return x**2 + x +2

mymin = minimize(min_bfgs, 0, method='BFGS')
print(mymin)

arr = np.array([0,0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))

arr_2d = np.array([
    [0,0,0],
    [0,0,1],
    [1,0,2]
])
print(csr_matrix(arr_2d).data)
mat = csr_matrix(arr_2d)
print("Convert to csc:\n", mat.tocsc())
'''
mat.sum_duplicates()
print("Eliminating duplicates:\n",mat)
mat.eliminate_zeros()
print("After eliminate zeros:\n",mat)
'''

graph_arr = np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0],
])

csr_graph_arr = csr_matrix(graph_arr)

print(csr_graph_arr)
print(connected_components(csr_graph_arr))
print(dijkstra(csr_graph_arr, return_predecessors=True, indices=0))
print(floyd_warshall(csr_graph_arr, return_predecessors=True))
print(bellman_ford(csr_graph_arr, return_predecessors=True, indices=0))
print(depth_first_order(csr_graph_arr, 1))

points = np.array([
    [2,4],
    [3,4],
    [3,0],
    [2,2],
    [4,1]
])

'''
simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:,1], simplices)
plt.scatter(points[:,0], points[:,1], color='r')

plt.show()
'''
from scipy import io
io.savemat('arr.mat', {'vec': arr})

print(io.loadmat('arr.mat', squeeze_me=True)['vec'])
