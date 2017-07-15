'''DFS-iterative (G, s):                                   //Where G is graph and s is source vertex
      let S be stack
      S.push( s )            //Inserting s in stack 
      mark s as visited.
      while ( S is not empty):
          //Pop a vertex from stack to visit next
          v  =  S.top( )
         S.pop( )
         //Push all the neighbours of v in stack that are not visited   
        for all neighbours w of v in Graph G:
            if w is not visited :
                     S.push( w )         
                    mark w as visited


    DFS-recursive(G, s):
        mark s as visited
        for all neighbours w of s in Graph G:
            if w is not visited:
                DFS-recursive(G, w)'''

from collections import defaultdict


def dfs(G,s):
    visited[s] = True
    global level
    for neighbor in G[s]:
        if visited[neighbor] is False:
            level[neighbor] = level[s]+1
            dfs(G,neighbor)

G = defaultdict(list)
countries = int(raw_input())
visited = [False] * (countries+1)
level = [0] * (countries+1)
level[1] = 0
for _ in xrange(countries-1):
    a, b = map(int,raw_input().split())
    G[a].append(b)
    G[b].append(a)

dfs(G,1)

n_girls = int(raw_input())
girls = []
for __ in xrange(n_girls):
    girls.append(int(raw_input()))

girls.sort()

print min(girls,key=lambda x:level[x])





