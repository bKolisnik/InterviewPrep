#!/bin/python3

import math
import os
import random
import re
import sys
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

#Determine the minimum cost to provide library access to all citizens of HackerLand. There are n cities numbered from 1 to n. Currently there are no libraries and the cities are not connected. Bidirectional roads may be built between any city pair listed in cities. A citizen has access to a library if:

#Their city contains a library.
#They can travel by road from their city to a city containing a library.


#finding connected components via dfs
class Graph:
    def __init__(self, pairs,v):
        #pairs are the 2d list of vetexes that share an edge
        
        #instead of using empty list, had to use empty set as the adjacency list for each vertex.
        self.g = [set() for i in range(v)]
        self.v = v
        for p in pairs:
            self.g[p[0]-1].add(p[1]-1)
            self.g[p[1]-1].add(p[0]-1)
            
    def dfs_visit(self, visited, source):
        #i is the source node 
        stack = deque()
        
        stack.append(source)
        
        while(stack):
            vert = stack.pop()
            if not visited[vert]:
                visited[vert]=True
            
            #get all adjacent vertices of the current vertex and add to stack
            for j in self.g[vert]:
                if not visited[j]:
                    stack.append(j)
        
    def count_components(self):
        visited = [False]*self.v
        num_connected_components = 0
        
        
        for i in range(self.v):
            if not visited[i]:
                #dfs visit will mutate the visited array and return the size of the connected component
                self.dfs_visit(visited, i)
                num_connected_components +=1
                
        return num_connected_components
        
# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    #if cost of library is less than cost of road than simply build a library in each city
    if c_lib < c_road:
        return n*c_lib
    
    #find number of connected components in graph, buy one library for each connected components
    #for each connected component let size be c buy c-1 roads.
    #let u be num_components then sigma(i=0 to u) (c_i-1) = sum(c_i) - u = n - u as sum of all component sizes is n
    graph = Graph(cities, n)
    num_connected_components = graph.count_components()
    return num_connected_components*c_lib + (n - num_connected_components)*c_road
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
